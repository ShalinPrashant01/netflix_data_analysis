import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("data/netflix_titles.csv")

# Show the first 5 rows
print(df.head())


import pandas as pd

# Load the dataset
df = pd.read_csv("data/netflix_titles.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show column names
print("\nColumn names:")
print(df.columns)

# Show basic info (rows, columns, datatypes, etc.)
print("\nInfo:")
print(df.info())

# Show summary statistics (only for numeric columns)
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())


# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Let's see which columns have missing data
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in 'country', 'cast', 'director' with 'Unknown'
df['country'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)

# Drop rows where 'date_added' or 'rating' is missing (optional)
df.dropna(subset=['date_added', 'rating'], inplace=True)

# 3. Convert 'date_added' to datetime format
# Remove leading/trailing spaces in date column
df['date_added'] = df['date_added'].str.strip()

# Convert to datetime format safely
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')



# 4. Trim extra spaces in column values (e.g., in 'type', 'rating')
df['type'] = df['type'].str.strip()
df['rating'] = df['rating'].str.strip()

# 5. Final check
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned data to a new CSV (optional but good for later steps)
df.to_csv("data/netflix_cleaned.csv", index=False)

print("\nData cleaned and saved successfully!")


import matplotlib.pyplot as plt
import seaborn as sns

# Optional: better style
sns.set(style="darkgrid")

# 1. TV Shows vs Movies count
plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Count of TV Shows vs Movies")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2. Top 10 countries by content
plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Ratings distribution
plt.figure(figsize=(10,5))
df['rating'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Content added by year
df['year_added'] = df['date_added'].dt.year
plt.figure(figsize=(10,5))
df['year_added'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Netflix Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.tight_layout()
plt.show()


print("\nTop 10 Directors:")
print(df['director'].value_counts().head(10))
