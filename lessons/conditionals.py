"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between 1 and 5. ")

guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
else:
    print("Sorry, you guessed incorrectly.")

print("Game over.")