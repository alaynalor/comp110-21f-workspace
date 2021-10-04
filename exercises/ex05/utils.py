"""List utility functions part 2."""

__author__ = "730411361"

# Define your functions below


def only_evens(input: list[int]) -> list[int]:
    """Return list of even ints in input."""
    evens: list[int] = []
    i: int = 0
    while i < len(input):
        if input[i] % 2 == 0:
            evens.append(input[i])
        i += 1
    return evens
    

def sub(input: list[int], start: int, end: int) -> list[int]:
    """Return list of input between start and end int."""
    subset: list[int] = []
    if len(input) == 0 or start > len(input) or end <= 0:
        return subset
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    while start < end:
        subset.append(input[start])
        start = start + 1
    return subset


def concat(a: list[int], b: list[int]):
    """Return list that includes a and b."""
    i: int = 0
    new: list[int] = []
    while i < len(a):
        new.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        new.append(b[i])
        i += 1
    return new