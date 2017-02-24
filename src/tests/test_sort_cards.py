"""Tests for sort_cards module."""
import pytest

SORT_TABLE = [
    ['39A5T824Q7J6K', 'A23456789TJQK'],
    ['Q286JK395A47T', 'A23456789TJQK'],
    ['54TQKJ69327A8', 'A23456789TJQK']
]


@pytest.mark.parametrize("cards, result", SORT_TABLE)
def test_sort_cards(cards, result):
    """Test the sort_cards function."""
    from sort_cards import sort_cards
    result = sort_cards(list(cards))
    expected = list(result)
    assert result == expected
