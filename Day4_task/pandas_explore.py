import pandas as pd

# Create DataFrame

students = {
    "name": [
        "Anshula", "Riya", "Arjun", "Priya", "Rahul",
        "Neha", "Karan", "Aman", "Sneha", "Vikram"
    ],
    "city": [
        "Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
        "Jaipur", "Delhi", "Chandigarh", "Mumbai", "Chandigarh"
    ],
    "math_score": [95, 82, 76, 68, 88, 91, 72, 85, 79, 93],
    "science_score": [92, 85, 80, 70, 90, 87, 75, 89, 81, 95],
    "english_score": [90, 78, 84, 72, 86, 93, 70, 88, 85, 91]
}

df = pd.DataFrame(students)

print("DataFrame:\n")
print(df)

# ------------------------------------------------
# 1. Average score in each subject
# ------------------------------------------------

print("\nAverage Score in Each Subject:")
print(df[["math_score", "science_score", "english_score"]].mean())

# ------------------------------------------------
# 2. Student with highest total score
# ------------------------------------------------

df["total_score"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
)

print("\nStudent with Highest Total Score:")
print(df.loc[df["total_score"].idxmax()])

# ------------------------------------------------
# 3. Number of students from each city
# ------------------------------------------------

print("\nStudents from Each City:")
print(df.groupby("city").size())

# ------------------------------------------------
# 4. Students with math score > 75
# ------------------------------------------------

print("\nStudents with Math Score Above 75:")
print(df[df["math_score"] > 75])

# ------------------------------------------------
# EXPLORE: Top 3 Students by Total Score
# ------------------------------------------------

print("\nTop 3 Students by Total Score:")
print(df.nlargest(3, "total_score"))