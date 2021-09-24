"""Number Guessing Game!"""
__author__ = "730411361"

from random import randint
number: int

player: str 
points: int
__name__ == "__main__"

correct_emoji: str = '\U0001F973'
incorrect_emoji: str = '\U0001F641'


def main() -> None:
    points = 0
    choice: str = input("Please select one of the following options: Start Game, See Player Status, End Game: ")
    if choice == "End Game":
        print("Thank you for playing, {player}! Have a great day!")
    if choice == "Start Game":
        game()
        main()
    if choice == "Player Status":
        if status(points) < 2:
            print(f"You have {points} points and is ranked with gold status.")
        else:
            if status(points) < 3:
                print(f"You have {points} points and is ranked with silver status.")
            else:
                print(f"You have {points} points and is ranked with bronze status.")
    main()
    choice = input("Please select one of the following options: Start Game, See Player Status, End Game: ")


def game() -> None:
    points = 0
    player = input("Please Insert Player Name: ")
    level: str = input("Choose a level: Easy, Medium, Hard: ")
    if level == "Easy":
        print(f"{player}, I am thinking of a number between 1 and 10.")
        number = randint(1, 10)
    if level == "Medium":
        print(f"{player}, I am thinking of a number between 1 and 25.")
        number = randint(1, 25)
    if level == "Hard":
        print(f"{player}, I am thinking of a number between 1 and 50.")
        number = randint(1, 50)
    tries_remaining: int = 5
    while tries_remaining > 0:
        if tries_remaining == 5:
            guess: int = int(input("Guess the number I am thinking of: "))
        tries_remaining = tries_remaining - 1
        if guess == number:
            print(f"Correct, {player}!{correct_emoji}")
            points = points + 1
            print(f"Total Points: {points}")
            tries_remaining = 0
        else:
            print(f"Sorry, {player}, that's incorrect {incorrect_emoji}")
            print(f"Total Points: {points}")
            print(f"Tries Remaining: {tries_remaining}")
            if guess < number:
                if tries_remaining == 0:
                    print(f"Sorry, {player}, you have run out of tries.")
                guess: int = int(input("Guess Again! ** Hint: It's higher! "))
            else:
                if tries_remaining == 0:
                    print(f"Sorry, {player}, you have run out of tries.")
                else:
                    guess: int = int(input("Guess Again! ** Hint: It's lower! "))
    

def greet() -> None:
    print("Weclcome to the number guessing game! Lets see how many points you can get by guessing correctly. You will be given 5 tries each round.")


def status(a: int) -> int:
    if a < 5:
        return (3)
    if a >= 5 and a < 10:
        return (2)
    else:
        return (3)

greet()
main()