"""Tests for shortest_word module."""
import pytest


XO_TABLE = [
    [['xo'], True],
    [['xo0'], True],
    [['xxxoo'], False]
]


@pytest.mark.parametrize("s, result", XO_TABLE)
def test_xo(s, result):
    """Test the xo function."""
    from xo import xo
    assert xo(s) == result
