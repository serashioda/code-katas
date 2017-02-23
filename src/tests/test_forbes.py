# -*- coding: UTF-8 -*-
"""Tests for forbes implementation."""
import pytest
from forbes import *


@pytest.fixture
def data():
    """Fixture to get jason data."""
    return get_json()


def test_billionaire_age_valid(data):
    """Test that find billionaire finds youngest billionaire with valid age."""
    result = find_billionaire(data)
    assert result['youngest_valid']['name'] == 'Mark Zuckerberg'
    assert result['youngest_valid']['age'] == 32


def test_billionaire_oldest(data):
    """Test that find billionaire finds oldest billionaire under 80."""
    result = find_billionaire(data)
    assert result['oldest_under_80']['name'] == 'Phil Knight'
    assert result['oldest_under_80']['age'] == 78


def test_billionaire_age_not_valid(data):
    """Verify that the smallest number in age is invalid and does not return as youngest billionaire."""
    result = find_billionaire(data)
    assert result['youngest_valid']['name'] != 'Beate Heister & Karl Albrecht Jr.'
    assert result['youngest_valid']['age'] != -1


def test_billionaire_age_0_is_valid(data):
    """Test that age 0 is a valid age."""
    data.append({
        'name': 'Adam Smith',
        'age': 0,
        'rank': 35,
        'net_worth (USD)': 100000000000,
        'source': 'baby food',
        'country': 'United States'
    })
    result = find_billionaire(data)
    assert result['youngest_valid']['name'] == 'Adam Smith'
    assert result['youngest_valid']['age'] == 0
