"""Tests for shortest_word module. """
import pytest

SHORT_TABLE = [
    [["bitcoin take over the world maybe who knows perhaps"], 3],
    [["turns out random test cases are easier than writing out basic ones"], 3],
    [["lets talk about javascript the best language"], 3],
    [["i want to travel the world writing code one day"], 1],
    [[""Lets all go on holiday somewhere very cold"], 2]
]


@pytest.mark.parametrize("s, result", SHORT_TABLE)
def test_shortest_word(s, result):
    """Test the find_short function."""
    from shortest_word import find_short
    assert find_short(s) == result
