#The Self-Intro Upgrade
#Introduction usinf different variables and then storing them in a separate dictionary and aslo usinf various built-in functions
name="Anshula"
age=20
city="Hoshiarpur"
favourite_subject="Data Science"
target_role="Data Scientist"

#Dictionary Creation
dct={
    "name": name,
    "age":age,
    "city":city,
    "favourite_subject":favourite_subject,
    "target_role":target_role
}

print(f"My name is {dct['name'].title()}.")
print(f"My age is {dct['age']}.")
print(f"I am from {dct['city'].title()}.")
print(f"My favourite Subject is {dct["favourite_subject"].title()}.")
print(f"The job role I am targeting is {dct["target_role"].title()}.")