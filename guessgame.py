import random

print("========== GUESS GAME ==========")

secret_number = random.randint(1, 100)

guess = int(input("Enter the number between 1 and 100: "))

print("Your guess:", guess)

if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")