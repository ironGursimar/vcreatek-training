import argparse
import os
import sys
from io import StringIO

import boto3
import pandas as pd

# S3 Configuration
BUCKET = "bucket121411"
INPUT_PREFIX = "input/"
OUTPUT_PREFIX = "output/"


def detect_type(series):
    """Detect whether a column is numeric, date, or text."""

    non_missing = series.dropna()

    if len(non_missing) == 0:
        return "text"

    if pd.api.types.is_numeric_dtype(series):
        return "numeric"

    date_series = pd.to_datetime(
        non_missing,
        errors="coerce",
        format="mixed"
    )

    if date_series.notna().all():
        return "date"

    return "text"


def profile_csv(file_path, top_n):
    """Read and profile a CSV file."""

    output = StringIO()

    try:
        df = pd.read_csv(file_path)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        sys.exit(1)

    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        sys.exit(1)

    except pd.errors.ParserError:
        print(f"Error: '{file_path}' is not a valid CSV file.")
        sys.exit(1)

    except Exception as error:
        print(f"Error: Could not read '{file_path}'.")
        print(f"Details: {error}")
        sys.exit(1)

    rows, columns = df.shape

    print(f"Rows: {rows}")
    print(f"Columns: {columns}")

    output.write(f"Rows: {rows}\n")
    output.write(f"Columns: {columns}\n")

    for column in df.columns:

        series = df[column]

        missing = series.isna().sum()

        if rows > 0:
            missing_percentage = (missing / rows) * 100
        else:
            missing_percentage = 0

        data_type = detect_type(series)

        print()
        print(f"Column: {column}")
        print(f"Type: {data_type}")
        print(f"Missing: {missing} ({missing_percentage:.2f}%)")

        output.write("\n")
        output.write(f"Column: {column}\n")
        output.write(f"Type: {data_type}\n")
        output.write(f"Missing: {missing} ({missing_percentage:.2f}%)\n")

        if data_type == "numeric":

            print(f"Min: {series.min()}")
            print(f"Mean: {series.mean():.2f}")
            print(f"Max: {series.max()}")

            output.write(f"Min: {series.min()}\n")
            output.write(f"Mean: {series.mean():.2f}\n")
            output.write(f"Max: {series.max()}\n")

        elif data_type == "text":

            print(f"Top {top_n} values:")
            output.write(f"Top {top_n} values:\n")

            top_values = (
                series
                .dropna()
                .value_counts()
                .head(top_n)
            )

            for value, count in top_values.items():
                print(f"  {value}: {count}")
                output.write(f"  {value}: {count}\n")

    return output.getvalue()


def main():

    parser = argparse.ArgumentParser(
        description="Profile CSV files from S3 input and save reports to S3 output."
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of most frequent text values to display (default: 5)"
    )

    args = parser.parse_args()

    if args.top <= 0:
        print("Error: --top must be greater than 0.")
        sys.exit(1)

    s3 = boto3.client("s3")

    response = s3.list_objects_v2(
        Bucket=BUCKET,
        Prefix=INPUT_PREFIX
    )

    if "Contents" not in response:
        print("No CSV files found in input/.")
        return

    for obj in response["Contents"]:

        key = obj["Key"]

        if not key.endswith(".csv"):
            continue

        filename = os.path.basename(key)

        print(f"\nProcessing {filename}...")

        report = profile_csv(
            f"s3://{BUCKET}/{key}",
            args.top
        )

        output_key = (
            f"{OUTPUT_PREFIX}"
            f"{filename.replace('.csv', '_stats.txt')}"
        )

        s3.put_object(
            Bucket=BUCKET,
            Key=output_key,
            Body=report
        )

        print(f"Uploaded to s3://{BUCKET}/{output_key}")

    print("\nAll CSV files processed successfully.")


if __name__ == "__main__":
    main()
