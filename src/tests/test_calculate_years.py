"""Tests for calculate_years module."""
import pytest

YEARS_TABLE = [
    [1000, 0.05, 0.18, 1100, 3],
    [1000, 0.01625, 0.18, 1200, 14],
    [1000, 0.05, 0.18, 1000, 0]
]


@pytest.mark.parametrize("principal, interest, tax, desired, result", YEARS_TABLE)
def test_calculate_years(principal, interest, tax, desired, result):
    """Test the calculate_years function."""
    from calculate_years import calculate_years
    assert calculate_years(principal, interest, tax, desired) == result
