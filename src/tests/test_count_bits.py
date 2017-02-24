"""Tests for count_bits module."""
import pytest

BITS_TABLE = [
    [0, 0],
    [4, 1],
    [7, 3],
    [9, 2],
]


@pytest.mark.parametrize("n, result", BITS_TABLE)
def test_count_bits(n, result):
    """Test the countBits function."""
    from count_bits import count_bits
    assert count_bits(n) == result
