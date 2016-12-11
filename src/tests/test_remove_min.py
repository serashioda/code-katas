"""Tests for remove_min module."""
import pytest

MIN_TABLE = [
    [[1, 2, 3, 4, 5], [2, 3, 4, 5]],
    [[5, 3, 2, 1, 4], [5, 3, 2, 4]],
    [[1, 2, 3, 1, 1], [2, 3, 1, 1]],
    [[], []]
]


@pytest.mark.parametrize("numbers, result", MIN_TABLE)
def test_remove_min(numbers, result):
    """Test the remove_smallest function."""
    from remove_min import remove_smallest
    assert remove_smallest(numbers) == result
