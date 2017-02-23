"""Tests for is_isogram module."""
import pytest

ISO_TABLE = [
    ["Dermatoglyphics", True],
    ["isogram", True],
    ["aba", False],
    ["moOse", False],
    ["isIsogram", False],
    ["", True]
]


@pytest.mark.parametrize("string, result", ISO_TABLE)
def test_is_isogram(string, result):
    """Test the is_isogram function."""
    from is_isogram import is_isogram
    assert is_isogram(string) == result
