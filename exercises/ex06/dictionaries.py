"""Practice with dictionaries."""

__author__ = "123456789"

# Define your functions below


def invert(input: dict[str, str]) -> dict[str, str]:
    """Returns dictionary with keys and values switched."""
    if input == {}:
        raise KeyError
    invert: dict[str, str] = {}
    for key in input:
        if input[key] in invert:
            raise KeyError
        else:
            invert[input[key]] = key
    return(invert)


def favorite_color(input: dict[str, str]) -> str:
    """Returns str of color that appears most in input."""
    if input == {}:
        raise KeyError
    new: dict[str, int] = dict()
    number: int = 0
    favorite: str = ""
    for key in input:
        if input[key] in new:
            new[input[key]] += 1
        else:
            new[input[key]] = 1
    for key in new:
        if new[key] > number:
            number = new[key]
            favorite = key
    return(favorite)


def count(input: list[str]) -> dict[str, int]:
    """Recturns dictionary with counts of str that appear in input."""
    if input == {}:
        raise KeyError
    answer: dict[str, int] = {}
    i: int = 0
    while i < len(input):
        if input[i] in answer:
            answer[input[i]] += 1
        else:
            answer[input[i]] = 1
        i += 1
    return answer