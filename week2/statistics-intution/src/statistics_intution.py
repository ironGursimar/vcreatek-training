
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load Dataset
df = pd.read_csv("WineQT.csv")

# -------------------------
# Task 1: Descriptive Statistics
# -------------------------

print("\n=== Dataset Information ===")
print(df.info())

print("\n=== Statistical Summary ===")
print(df.describe())

print("\n=== Alcohol Statistics ===")
print("Mean:", df["alcohol"].mean())
print("Median:", df["alcohol"].median())
print("Standard Deviation:", df["alcohol"].std())

print("25th Percentile:", df["alcohol"].quantile(0.25))
print("50th Percentile:", df["alcohol"].quantile(0.50))
print("75th Percentile:", df["alcohol"].quantile(0.75))

# -------------------------
# Task 2: Distribution
# -------------------------

plt.figure(figsize=(8,5))
plt.hist(df["alcohol"], bins=20)
plt.title("Distribution of Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,4))
plt.boxplot(df["alcohol"], vert=False)
plt.title("Boxplot of Alcohol Content")
plt.xlabel("Alcohol")
plt.show()

print("Skewness:", df["alcohol"].skew())

# -------------------------
# Task 3: Correlation
# -------------------------

corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()

strongest_pair = (
    corr_matrix.where(~np.eye(corr_matrix.shape[0], dtype=bool))
    .stack()
    .abs()
    .idxmax()
)

print("Strongest Correlated Pair:", strongest_pair)
print("Correlation Value:", corr_matrix.loc[strongest_pair])

# -------------------------
# Task 4: Hypothesis Testing
# -------------------------

low_quality = df[df["quality"] < 6]["alcohol"]
high_quality = df[df["quality"] >= 6]["alcohol"]

t_stat, p_value = ttest_ind(high_quality, low_quality)

print("\n=== Hypothesis Testing ===")
print("T-statistic:", t_stat)
print("P-value:", p_value)

print("Mean Alcohol (High Quality):", high_quality.mean())
print("Mean Alcohol (Low Quality):", low_quality.mean())

if p_value < 0.05:
    print("Reject the Null Hypothesis.")
else:
    print("Fail to Reject the Null Hypothesis.")
