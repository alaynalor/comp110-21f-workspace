"""List utility functions."""

__author__ = "123456789"

# TODO: Implement your functions here.


def all(a: list[int], b: int) -> bool:
    """Return True if all values in list are equal to given integer."""
    i: int = 0
    if len(a) == 0:
        return (False)
    while i < len(a):
        if b != a[i]:
            return (False)
        i =+ 1
    return (True)


def is_equal(c: list[int], d: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if len(c) != len(d):
        return (False)
    i: int = 0
    while i < len(c) and i < len(d):
        if c[i] != d[i]:
            return(False)
        i =+ 1
    return (True)


def max(input: list[int]) -> int:
    """Return the max integer in given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    answer = int
    i: int = 0 
    while i < len(input):
        if input[i] < input[i + 1]:
            answer = input[i + 1] 
        else:
            answer = input[i]
        i = + 1
    return (int(answer))