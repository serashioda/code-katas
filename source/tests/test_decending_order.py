"""Tests for decending_order module."""
import pytest

LIST_TABLE = [
    [[13256], 65321],
    [[10585], 85510],
    [[15], 51],
    [[153], 531]],
    [[123456789], 987654321]
]


@pytest.mark.parametrize("num, result", LIST_TABLE)
def decending_order(num, result):
    """Test the decending_order function."""
    from decending_order import decending_order
    assert decending_order(num) == result
