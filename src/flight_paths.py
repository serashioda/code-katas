"""Implementation of the flight path module."""
from math import radians, cos, sin, asin, sqrt
from shortest_path_stack import Graph
import json

'''
given a starting city and an ending city, will:
1) return a path between the two cities (including the two cities).
2) returns the total distance traveled between cities.
3) appropriately handles the situation where no path exists.
Stretch Goals:
Incorporate any(or all) of these. They are/can be independent of each other:
1) Add to your function a parameter that makes it return the shortest path
   (lowest distance) between the two cities.
2) Add to your function a parameter that makes it return the path with the
   fewest stops between the two cities.
3) Have your function take a parameter for a limit to the distance between any
   two cities.
   - If specified, your function returns a path where each city-to-city jump is
     less than or equal to that limit.
'''


def haversine(lon1, lat1, lon2, lat2):
    """Calculate circle distance between two points on the earth."""
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def get_data(filename):
    """Grab JSON data."""
    s = open(filename, 'r').read()
    data = json.loads(s)
    return data


def get_airport(data, city):
    """Grab airport data by aiport key."""
    for airport in data:
        if airport['airport'] == city:
            return airport
    return None


def find_shortest_path(source, destination, data):
    """Find the shortest path between two existing points, otherwise raise exception."""
    g = Graph()
    for airport in data:
        g.add_node(airport['airport'])

        for destination_city in airport["destination_airports"]:

            d_airport = get_airport(data, destination_city)

            if d_airport is not None:
                distance = haversine(airport['lat_lon'][1], airport['lat_lon'][0], d_airport['lat_lon'][1], d_airport['lat_lon'][0])
                try:
                    g.add_edge(airport['airport'], d_airport['airport'], distance)
                except Exception as e:
                    next

    # Dictionary is packed, ready for depth finding
    path = g.dijkstra(destination, source)
    distance = 0
    for i in range(0, len(path) - 2):
        airport = get_airport(data, path[i])
        d_airport = get_airport(data, path[i + 1])
        distance += haversine(airport['lat_lon'][1], airport['lat_lon'][0], d_airport['lat_lon'][1], d_airport['lat_lon'][0])

    if distance <= 0:
        raise ValueError("That path does not exist")

    result = {
        "path": path,
        "distance": distance
    }

    return result
