# Task 2: Extract a Small Report from a JSON File
# Reads a JSON file and prints a short report.

import json

# Load JSON data
with open("student.json", "r") as file:
    data = json.load(file)

# List comprehension to transform skills
skills_upper = [skill.upper() for skill in data["skills"]]

# Print report
print(f"Name   : {data['name']}")
print(f"Role   : {data['role']}")
print(f"Skills : {', '.join(skills_upper)}")