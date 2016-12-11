"""Tests for find_odd_int module."""
import pytest

FIND_TABLE = [
    [[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5],
    [[15, 3, 5, 5, 2, 5, 1, 15, 3], 5]
]


@pytest.mark.parametrize("seq, result", FIND_TABLE)
def test_find_odd_int(seq, result):
    """Test the find_it function."""
    from find_odd_int import find_it
    assert find_it(seq) == result
