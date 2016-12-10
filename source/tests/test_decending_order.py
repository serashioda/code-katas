""Tests for decending_order module."""
import pytest

LIST_TABLE = [
    [[13256], 65321],
    [[10585], 85510],
    [[12], 21],
    [[153], 531]]
]


@pytest.mark.parametrize("num, result", LIST_TABLE)
def decending_order(num, result):
    """Test the decending_order function."""
    from decending_order import decending_order
    assert decending_order(num) == result
