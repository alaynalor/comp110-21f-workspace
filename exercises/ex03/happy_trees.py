"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
<<<<<<< HEAD
number: int = 1

while depth > 0:
    print(TREE * number)
    depth = depth - 1
    number = number + 1
=======

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
