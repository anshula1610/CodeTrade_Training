import csv

students_data = [
    ["name", "math", "science", "english"],
    ["Anshula", 95, 88, 92],
    ["Riya", 78, 82, 80],
    ["Arjun", 65, 70, 68]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("students.csv created successfully.")

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math = int(row["math"])
        science = int(row["science"])
        english = int(row["english"])

        average = (math + science + english) / 3
        grade = get_grade(average)

        results.append({
            "name": row["name"],
            "average": round(average, 2),
            "grade": grade
        })

with open("results.csv", "w", newline="") as file:
    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("results.csv generated successfully.")