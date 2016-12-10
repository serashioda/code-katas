""Tests for shortest_word module."""
import pytest

XO_TABLE = [
    [[xo], 'xo'],
    [[xo], 'xo0']],
    [[not xo], 'xxxoo']
]


@pytest.mark.parametrize("s, result", XO_TABLE)
def xo(s, result):
    """Test the xo function."""
    from xo import xo
    assert xo(s) == result
