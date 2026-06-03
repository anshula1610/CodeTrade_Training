import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Set Name as index for .loc demonstration
df = df.set_index("Name")

print("Dataset:")
print(df)

# ---------------------------
# .loc Example (Label-Based)
# ---------------------------
print("\nUsing .loc")

loc_selection = df.loc[
    ["Anshula", "Neha"],      # Row labels
    ["Course", "Score"]       # Column labels
]

print(loc_selection)

print("\nUsing .iloc")

iloc_selection = df.iloc[
    [0, 4],      # Row positions
    [1, 2]       # Column positions
]

print(iloc_selection)