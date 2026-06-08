import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Starting Program...")

df = pd.read_csv("kc_house_data.csv")

print("Dataset Shape:", df.shape)

print("Checking Missing Values...")
print(df.isnull().sum())

# Heatmap
print("Creating Heatmap...")

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# Histogram
print("Creating Histogram...")

plt.figure(figsize=(8, 5))
sns.histplot(df["price"], bins=30)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.savefig("histogram.png")
plt.show()

print("Program Finished Successfully!")