#program to check whether the given number is even or odd
#print the message invalid input if anything without the number is being entered


#int() converts a string into an integer
# If we give int() to a String like "abc" then error is occured

num1=int(input("Enter the number:"))
if num1%2==0:
    print(f"The number {num1} is even")
elif num1==0:
    print("The number is zero")
elif num1%2 != 0:
    print(f"The number {num1} is odd")
else:
    print("Invalid Number")




try:
    num=int(input("Enter the number to be checked:"))
    if num%2==0:
        print(f"The number {num} is even")
    elif num==0:
        print("The number is zero")
    elif num%2 != 0:
        print(f"The number {num} is odd")
except ValueError:
    print("Invalid input")