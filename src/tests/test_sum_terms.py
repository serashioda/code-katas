"""Tests for sum_terms module."""
import pytest

TERMS_TABLE = [
    [1, '1.00'],
    [2, '1.25'],
    [3, '1.39']
]


@pytest.mark.parametrize("n, result", TERMS_TABLE)
def test_sum_terms(n, result):
    """Test the series_sum function."""
    from sum_terms import series_sum
    assert series_sum(n) == result
