from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        common = gcd(self.numerator, self.denominator)

        self.numerator //= common
        self.denominator //= common

        # Keep denominator positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_num = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        new_den = self.denominator * other.denominator

        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )


# -------------------------
# Test Case 1: Addition
# -------------------------

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print("Fraction 1:", f1)
print("Fraction 2:", f2)
print("Addition:", f1 + f2)

# -------------------------
# Test Case 2: Equality
# -------------------------

f3 = Fraction(2, 4)
f4 = Fraction(1, 2)

print("\nEquality Test:")
print(f3, "==", f4, ":", f3 == f4)

# -------------------------
# Test Case 3: Comparison
# -------------------------

f5 = Fraction(3, 5)
f6 = Fraction(4, 5)

print("\nLess Than Test:")
print(f5, "<", f6, ":", f5 < f6)