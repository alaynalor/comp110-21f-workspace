"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert_one() -> None:
    """Testing with one dictionary entry."""
    assert invert({"alayna": "lorenzana"}) == {"lorenzana": "alayna"}


def test_invert_two() -> None:
    """Testing with multiple dictionary entries."""
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_three() -> None:
    """Testing with multiple entries."""
    assert invert({"alayna": "yes", "carly": "no"}) == {"yes": "alayna", "no": "carly"}


def test_favorite_color_one() -> None:
    """Testing with multiple dictionary entries."""
    assert favorite_color({"Alayna": "purple", "Katie": "orange", "Logan": "blue", "Anna": "green", "Ashley": "purple"}) == "purple"


def test_favorite_color_two() -> None:
    """Testing with multiple of same color with same amount."""
    assert favorite_color({"Jim": "blue", "Riley": "orange", "Kyle": "black"}) == "blue"


def test_favorite_color_three() -> None:
    """Testing with one entry."""
    assert favorite_color({"Alayna": "blue"}) == "blue"


def test_count_one() -> None:
    """Testing with multiple list entries."""
    assert count(["blue", "red", "orange", "yellow", "blue"]) == {"blue": 2, "red": 1, "orange": 1, "yellow": 1}


def test_count_two() -> None:
    """Testing with multiple of same color."""
    assert count(["blue", "blue", "blue", "red", "blue"]) == {"blue": 4, "red": 1}


def test_count_three() -> None:
    """Testing with one list entry."""
    assert count(["blue"]) == {"blue": 1}