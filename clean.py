import pandas as pd

# Load the data
df = pd.read_csv("SampleSuperstore.csv")

# Step 1: Remove duplicates
df = df.drop_duplicates()

# Step 2: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Save cleaned data
df.to_csv("SampleSuperstore_cleaned.csv", index=False)

print(" Cleaning complete. Saved as 'SampleSuperstore_cleaned.csv'")