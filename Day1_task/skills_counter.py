# Using for loop print the skills being numbered and also print the total count of all the skills at the end
#using enumerate() function
lst=["Python","SQL","Java","Painting","Singing"]
for index,skill in enumerate(lst,start=1):
    print(f"{index}. {skill}")

print(f"Total skills: {len(lst)}")