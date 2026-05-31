
numbers = [5, 9, 12, 17, 18, 21, 25, 27, 30, 34,
           36, 40, 42, 45, 49, 51, 54, 58, 60, 63]

divisible_by_3 = [num for num in numbers if num % 3 == 0]

print("Numbers divisible by 3:")
print(divisible_by_3)

words = ["python", "java", "programming", "code",
         "developer", "data", "science"]

long_words = [word.title() for word in words if len(word) > 4]

print("\nWords longer than 4 characters in title case:")
print(long_words)

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

flattened = [num for sublist in nested_list for num in sublist]

print("\nFlattened list:")
print(flattened)

squares = {num: num**2 for num in range(1, 6)}

print("\nDictionary Comprehension:")
print(squares)


unique_lengths = {len(word) for word in words}

print("\nSet Comprehension:")
print(unique_lengths)