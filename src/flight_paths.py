"""Implementation of the flight path module."""
from shortest_path import Graph
'''
given a starting city and an ending city, will:
1) return a path between the two cities (including the two cities).
2) returns the total distance traveled between cities.
3) appropriately handles the situation where no path exists.
Stretch Goals:
Incorporate any(or all) of these. They are/can be independent of each other:
1) Add to your function a parameter that makes it return the shortest path (lowest distance) between the two cities.
2) Add to your function a parameter that makes it return the path with the fewest stops between the two cities.
3) Have your function take a parameter for a limit to the distance between any two cities. 
   - If specified, your function returns a path where each city-to-city jump is less than or equal to that limit.
'''


def get_data(filename):
    """Grab JSON data."""
    s = open(filename, 'r').read()
    data = json.loads(s)
    return data


def find_shortest_path(source, destination, data):
    """."""