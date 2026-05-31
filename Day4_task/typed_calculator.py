from typing import Optional


def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Returns:
        float: Sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.

    Returns:
        float: Difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Returns:
        float: Product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """
    Divides the first number by the second.

    Returns:
        float: Quotient if b is not zero.
        None: If division by zero is attempted.
    """
    if b == 0:
        return None

    return a / b


def power(base: float, exp: float) -> float:
    """
    Raises a number to a given power.

    Returns:
        float: base raised to exp.
    """
    return base ** exp


def modulo(a: int, b: int) -> Optional[int]:
    """
    Finds the remainder when a is divided by b.

    Returns:
        int: Remainder if b is not zero.
        None: If modulo by zero is attempted.
    """
    if b == 0:
        return None

    return a % b


# Test Cases

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by Zero:", divide(10, 0))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))
print("Modulo by Zero:", modulo(10, 0))