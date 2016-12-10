""Tests for multiply module."""
import pytest

LIST_TABLE = [
    [[1, 2, 3, 4, 5], 15],
    [[1, -2, 3, 4, 5], 13],
    [[-1, 2, 3, 4, -5], 9],
    [[-1, -4, -7], 0]
]


@pytest.mark.parametrize("lst, result", LIST_TABLE)
def test_sum_multiply(lst, result):
    """Test the multiply function."""
    from multiply import multiply
    assert multiply(lst) == result
