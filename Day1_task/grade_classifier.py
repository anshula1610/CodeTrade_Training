students=[
    {"name": "Anshula", "score": 92},
    {"name": "Rahul", "score": 76},
    {"name": "Priya", "score": 64},
    {"name": "Aman", "score": 48},
    {"name": "Sneha", "score": 35}
]
def classify(score):

    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 40:
        return "D"

    else:
        return "F"
sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)
for student in sorted_students:
    grade = classify(student["score"])

    print(
        f"Name: {student['name']}, "
        f"Score: {student['score']}, "
        f"Grade: {grade}"
    )