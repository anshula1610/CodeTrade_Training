import random

# Random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:

    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!\n")

        elif guess > secret_number:
            print("Too high!\n")

        else:
            print(
                f"Correct! You guessed the number "
                f"in {attempts} attempts."
            )
            break

    except ValueError:
        print("Please enter a valid number.\n")

else:
    print(
        f"Game Over! The correct number was "
        f"{secret_number}."
    )