# Task 3: Create a Tiny Class with a Useful Method
# This program defines a Learner class and displays learner information.

class Learner:
    def __init__(self, name: str, course: str, skill: str):
        self.name = name
        self.course = course
        self.skill = skill

    def get_profile(self) -> str:
        return (
            f"Learner Name : {self.name}\n"
            f"Course       : {self.course}\n"
            f"Top Skill    : {self.skill}"
        )


# Create an object
student = Learner(
    "Anshula",
    "Artificial Intelligence and Data Science",
    "Python"
)

# Call the method and print the result
print(student.get_profile())