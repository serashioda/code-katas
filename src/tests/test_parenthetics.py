"""Tests for parenthetics module."""


import pytest


PAREN_TABLE = [
    ['((()))', 0],
    ['((())', 1],
    [')))(((', -1]
]


@pytest.mark.parametrize("uni_string, result", PAREN_TABLE)
def test_parenthetics(uni_string, result):
    """Test the parenthetics function."""
    from parenthetics import parenthetics
    assert parenthetics(uni_string) == result


def test_pop_empty():
    """Test the parenthetics function."""
    from parenthetics import LinkedList
    list = LinkedList()
    try:
        list.pop()
    except Exception as e:
        assert str(e) == 'cannot pop from empty list'
