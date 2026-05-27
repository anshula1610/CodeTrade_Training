# contact_book.py

contacts = [
    {
        "name": "Alex",
        "phone": "9876543210",
        "email": "alex@gmail.com"
    },

    {
        "name": "Anshula",
        "phone": "9123456780",
        "email": "anshula@gmail.com"
    },

    {
        "name": "Priya",
        "phone": "9988776655",
        "email": "priya@gmail.com"
    },

    {
        "name": "Rahul",
        "phone": "9871234560",
        "email": "rahul@gmail.com"
    },

    {
        "name": "Sneha",
        "phone": "9012345678",
        "email": "sneha@gmail.com"
    }
]


def find_contact(name):

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found."


search_name = input("Enter contact name to search: ")

result = find_contact(search_name)

print(result)