"""Repeating a beat in a loop."""

__author__ = "730411361"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))

if number > 0:
    print((beat + " ") * (number-1) + beat)

else:
    print("No beat...")