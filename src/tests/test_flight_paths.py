"""Tests for flight path implementation."""
import pytest
from flight_paths import find_shortest_path, get_data


@pytest.fixture
def data():
    """Fixture to get jason data."""
    return get_data('src/flight_paths.json')


def test_finding_path(data):
    """Test that finds shortest path."""
    find_shortest_path('Jomo Kenyatta International Airport', 'London City Airport', data)


def test_finding_path_not_valid(data):
    """Test that invalid destination throws exception."""
    with pytest.raises(ValueError):
        find_shortest_path('Jomo Kenyatta International Airport', 'Ghost Town', data)
