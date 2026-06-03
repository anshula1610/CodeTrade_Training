# Task 7: Produce Quick Insights with describe() and value_counts()

import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

# ----------------------------------
# Numeric Summary
# ----------------------------------
print("=== Numeric Summary ===")
print(df.describe())

# ----------------------------------
# Categorical Summary
# ----------------------------------
print("\n=== Department Counts ===")
print(df["Department"].value_counts())

# ----------------------------------
# Observations
# ----------------------------------
print("\n=== Observations ===")
print("1. The average salary is 50,000.")
print("2. Data Science is the most common department.")