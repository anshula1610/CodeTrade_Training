# Task 1: Student Profile Card
# This program creates and displays a learner profile using
# variables, a dictionary, type hints, and f-strings.

name = "Anshula"
age = 19
course = "Artificial Intelligence and Data Science"

student_profile = {
    "college": "Arya College of Engineering and IT",
    "city": "Jaipur",
    "skill": "Python"
}


def create_profile_card(
    name: str,
    age: int,
    course: str,
    profile: dict
) -> str:
    """Returns a formatted student profile card."""

    return (
        f"Name   : {name}\n"
        f"Age    : {age}\n"
        f"Course : {course}\n"
        f"Skill  : {profile['skill']}"
    )


print(create_profile_card(name, age, course, student_profile))