# Task 4: Select Specific Columns and Filter Rows from a DataFrame
# Loads a CSV file, selects columns, and filters rows.

import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Select specific columns
selected_columns = df[["Name", "Course", "Score"]]

print("Selected Columns:")
print(selected_columns)

print("\nFilter: Students enrolled in Data Science")
filter_course = df[df["Course"] == "Data Science"]
print(filter_course)

print("\nFilter: Students with Score greater than 80")
filter_score = df[df["Score"] > 80]
print(filter_score)

print("\nFilter: Data Science students with Score greater than 80")
combined_filter = df[
    (df["Course"] == "Data Science") &
    (df["Score"] > 80)
]
print(combined_filter)