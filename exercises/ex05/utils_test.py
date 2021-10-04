"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730411361"


def test_only_evens_one() -> None:
    """Testing regular list."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_two() -> None:
    """Testing list with no evens."""
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_only_evens_three() -> None:
    """Testing empty list."""
    assert only_evens([]) == []


def test_sub_one() -> None:
    """Testing empty list."""
    assert sub([], 1, 1) == []


def test_sub_two() -> None:
    """Testing with negative start int."""
    assert sub([1, 1, 1, 1], -5, 1) == [1]


def test_sub_three() -> None:
    """Testing regular ascending list."""
    assert sub([1, 2, 3, 4], 0, 2) == [1, 2]


def test_concat_one() -> None:
    """Testing regular ascending lists."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Testing empty lists."""
    # passed
    assert concat([], []) == []


def test_concat_three() -> None:
    """Testing lists of different lengths."""
    assert concat([3], [2, 1]) == [3, 2, 1]