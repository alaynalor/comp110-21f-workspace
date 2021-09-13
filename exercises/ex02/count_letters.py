"""Counting letters in a string."""

__author__ = "730411361"

# Begin your solution here...

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
count: int = 0
character: str = (word[-i])


answer: bool = letter == character

while i < len(word):
    if answer == True:
        count = count + 1
        i = i + 1
    else:
        i = i + 1

print("Count: " + str(count))
