def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    if(b==0):
        return "Error: Division by zero"
    return a/b
def multiply(a,b):
    return a*b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    operation=input("choose operation (add/subtract/multiply/divide):").lower()

    if operation in operations:
        result = operations[operation](num1, num2)
        print(f"Result: {result}")

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numbers.")
