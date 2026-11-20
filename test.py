import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

while True:
    try:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed {secret_number} correctly.")
            break
    except ValueError:
        print("Please enter a valid whole number.")
