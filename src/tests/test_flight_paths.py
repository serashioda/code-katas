"""Tests for flight path implementation."""
import pytest
from flight_paths import find_shortest_path, get_data

# we define this here so parsing only has to occur once
data = get_data('src/flight_paths.json')


def test_finding_direct_path():
    """Test direct flight path."""
    result = find_shortest_path('Pointe Noire Airport', 'Cadjehoun Airport', data)
    assert result['distance'] == 1628.3270515412803
    assert result['path'] == ['Pointe Noire Airport', 'Cadjehoun Airport']


def test_finding_one_layover_path():
    """Test that finds shortest path with one layover."""
    result = find_shortest_path('Jomo Kenyatta International Airport', 'London City Airport', data)
    assert result['distance'] == 6839.011446262263
    assert result['path'] == ['Jomo Kenyatta International Airport', 'Zurich Airport', 'London City Airport']


def test_finding_two_layover_path():
    """Test that finds shortest path with two layovers."""
    result = find_shortest_path('Cadjehoun Airport', 'Melbourne Airport', data)
    assert result['distance'] == 15565.653079264486
    assert result['path'] == ['Cadjehoun Airport', 'OR Tambo International Airport', 'Perth Airport', 'Melbourne Airport']


def test_finding_path_when_start_and_destination_points_are_same():
    """Test that finds shortest path when flying to and from same point fails."""
    with pytest.raises(ValueError):
        find_shortest_path('London City Airport', 'London City Airport', data)


def test_finding_path_not_valid():
    """Test that invalid destination throws exception."""
    with pytest.raises(ValueError):
        find_shortest_path('Jomo Kenyatta International Airport', 'Ghost Town', data)


def test_none_for_each_arg_fails():
    """Test that the function rejects None for any parameter."""
    with pytest.raises(ValueError):
        find_shortest_path(None, 'Meow Town', data)
    with pytest.raises(ValueError):
        find_shortest_path('Meow Town', None, data)
    with pytest.raises(ValueError):
        find_shortest_path('Meow Town', 'Bark Town', None)


def test_emptystring_for_source_destination():
    """Test that the function rejects None for any parameter."""
    with pytest.raises(ValueError):
        find_shortest_path('', 'Meow Town', data)
    with pytest.raises(ValueError):
        find_shortest_path('Meow Town', '', data)
