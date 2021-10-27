"""Program that outputs one of at least four random, good fortunes."""

<<<<<<< HEAD
__author__ = "730411361"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

<<<<<<< HEAD
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
=======
# Begin your solution here...

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
