import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_data.csv")

print(df.shape)
print(df.info())
print(df.describe())

# Convert Price from text to numeric
# Convert Price from text to numeric
df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
print(df["Price"].dtype)
# Convert rating to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

print(df["Rating"].dtype)

print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# Price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=8, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.show()

# Boxplot for detecting price outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Price"])
plt.title("Boxplot of Book Prices")
plt.xlabel("Price (£)")
plt.show()

# Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating", data=df)
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.show()
# Relationship between Price and Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Rating", y="Price", data=df)

plt.title("Relationship Between Book Rating and Price")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.show()

# Correlation between Price and Rating
correlation = df["Price"].corr(df["Rating"])
print("Correlation between Price and Rating:", correlation)