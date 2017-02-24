"""Implementation of the forbes module."""
import json


def get_json():
    """Grab json data."""
    s = open('src/forbes.json', 'r').read()
    data = json.loads(s)
    return data


"""Write a function that returns the name, net worth, and industry of:
1) the oldest billionaire under 80 years old, AND
2) the youngest billionaire with a valid age.

STRETCH: Write another function that takes the company owned by the oldest under 80 and youngest billionaire, and
1) scrapes the web for its current stock price.
2) If the company is not public, have an appropriate message.
3) If the company is not an actual company, have an appropriate message.
"""


def find_billionaire(data):
    """Find both oldest under 80 and youngest valid billionaires using the two helper methods."""
    result = {
        'oldest_under_80': forbes_find_oldest_under_80(data),
        'youngest_valid': forbes_find_youngest_valid_age(data)
    }
    return result


def forbes_find_oldest_under_80(data):
    """Find the oldest billionaire under 80."""
    curr = data[0]
    for person in data:
        if person['age'] < 80 and curr['age'] < person['age']:
            curr = person
    return curr


def forbes_find_youngest_valid_age(data):
    """Find the youngest billionaire with a valid age."""
    curr = data[0]
    for person in data:
        if person['age'] >= 0 and person['age'] < curr['age']:
            curr = person
    return curr
