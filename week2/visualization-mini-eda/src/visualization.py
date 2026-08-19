import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load dataset
df = pd.read_csv("data/winequality-red.csv")

# Dataset overview
print(df.info())
print(df.describe())

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["alcohol"], bins=15, edgecolor="black")
plt.title("Distribution of Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(8,3))
plt.boxplot(df["alcohol"], vert=False)
plt.title("Boxplot of Alcohol Content")
plt.xlabel("Alcohol")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["alcohol"], df["sulphates"])
plt.title("Alcohol vs Sulphates")
plt.xlabel("Alcohol")
plt.ylabel("Sulphates")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())
