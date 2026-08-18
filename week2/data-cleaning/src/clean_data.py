import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/employee_data.csv")

# -----------------------------
# Data Type Conversion
# -----------------------------
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")

# -----------------------------
# Handle Missing Values
# -----------------------------
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# -----------------------------
# Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Detect and Remove Outliers (IQR)
# -----------------------------
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["Salary"] >= lower) & (df["Salary"] <= upper)]

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("data/employee_data_cleaned.csv", index=False)

print("Data cleaning completed successfully!")
print("\nFinal Dataset:")
print(df)

print("\nDataset Info:")
print(df.info())

# Optional Boxplot
plt.figure(figsize=(6,4))
plt.boxplot(df["Salary"])
plt.title("Salary After Cleaning")
plt.ylabel("Salary")
plt.show()
