"""Tests for flight path implementation."""
import pytest
from flight_paths import *


@pytest.fixture
def data():
    """Fixture to get jason data."""
    return get_data('src/flight_paths.json')


def test_finding_path(data):
    """Test that finds shortest path."""
    find_shortest_path('Goma', 'Kisangani', data)
