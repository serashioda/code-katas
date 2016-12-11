"""Tests for is_isogram module."""
import pytest

ISO_TABLE = [
    [["Dermatoglyphics"], True],
    [["isogram"], True]],
    [["aba"], False, "same chars may not be adjacent"],
    [["moOse"], False, "same chars may not be same case"],
    [["isIsogram"], False ],
    [[""], True, "an empty string is a valid isogram"]
]


@pytest.mark.parametrize("string, result", ISO_TABLE)
def test_is_isogram(string, result):
    """Test the is_isogram function."""
    from is_isogram import is_isogram
    assert is_isogram(string) == result
