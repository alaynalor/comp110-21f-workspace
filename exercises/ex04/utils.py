"""List utility functions."""

__author__ = "123456789"

# TODO: Implement your functions here.


def all(a: list[int], b: int) -> bool:
    """Return True if all values in list are equal to given integer."""
    if len(a) == 0:
        return(False)
    i: int = 0
    while i < len(a):
        if b != a[i]:
            return(False)
        i = + 1
    return(True)


def is_equal(c: list[int], d: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if len(c) != len(d):
        return(False)
    i: int = 0
    while i < len(c) or i < len(d):
        if c[i] != d[i]:
            return(False)
        i = + 1
    return(True)


def max(input: list[int]) -> int:
    """Return the max integer in given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    answer: int = input[0]
    while i < len(input):
        if input[i] >= input[i]:
            answer = input[i]
        i = + 1
    return(answer)