"""Tests for multiply module."""
import pytest

MULT_TABLE = [
    [2, 3, 6],
    [-2, 3, -6],
    [11, 5, 55],
    [3, 0, 0]
]


@pytest.mark.parametrize("a, b, result", MULT_TABLE)
def test_multiply(a, b, result):
    """Test the multiply function."""
    from multiply import multiply
    assert multiply(a, b) == result
