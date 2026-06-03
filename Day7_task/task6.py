# Task 6: Clean Missing Values and Inspect the Dataset

import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

print("Original Dataset:")
print(df)

# --------------------------------
# Check Missing Values
# --------------------------------
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# --------------------------------
# Case 1: dropna()
# Removes rows containing any missing value
# --------------------------------
df_dropna = df.dropna()

print("\nDataset After dropna():")
print(df_dropna)

# --------------------------------
# Case 2: fillna()
# Fill missing Age with average age
# Fill missing Department with 'Unknown'
# Fill missing Salary with average salary
# --------------------------------
df_fillna = df.copy()

df_fillna["Age"] = df_fillna["Age"].fillna(df_fillna["Age"].mean())
df_fillna["Department"] = df_fillna["Department"].fillna("Unknown")
df_fillna["Salary"] = df_fillna["Salary"].fillna(df_fillna["Salary"].mean())

print("\nDataset After fillna():")
print(df_fillna)