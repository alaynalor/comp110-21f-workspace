"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730411361"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

a: int = randint(1,4)

print("Your fortune cookie says...")

if a == 1:
    print("You will recieve good news soon!")

else:
    if a == 2:
        print("You will live a long a prosperous life!")
    else: 
        if a == 3:
            print("You will soon be rewarded for your accomplishments!")
        else:
            print("Embrace the change you will soon see in your life!")

print("Now, go spread positive vibes!")