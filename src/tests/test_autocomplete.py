"""Tests for autocomplete module."""
import pytest

TEST_TABLE = [
    ['f', ['fix', 'fax', 'fit', 'fist']],
    ['fi', ['fix', 'fit', 'fist', 'finch']],
    ['fin', ['finch', 'final', 'finial']],
    ['finally', []]
]


@pytest.mark.parametrize("n, result", TEST_TABLE)
def test_autocomplete(n, result):
    """Test the series_sum function."""
    from autocomplete import AutoCompleter
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = AutoCompleter(vocabulary, max_completions=4)
    assert complete_me.complete(n) == result
