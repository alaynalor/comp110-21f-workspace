"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
__author__ = "730411361"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

# Begin your solution here...

<<<<<<< HEAD
number: int = int(input("Enter an int: "))

if number % 2 == 0:
    if number % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")

else:
    if number % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")
      
=======
# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
