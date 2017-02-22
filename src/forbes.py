"""."""

import json
s = open('forbes.json', 'r').read()
data = json.loads(s)
print(data)


# returns the name, net worth, and industry of the oldest billionaire under 80 years old AND the youngest billionaire with a valid age.


def forbes_find_oldest_under_80(data):
    """Find the oldest billionaire under 80."""
    curr = data[0]
    for person in data:
        if person['age'] < 80 and curr['age'] < person['age']:
            curr = person
    return curr
result = forbes_find_oldest_under_80(data)
print(result)


def forbes_find_youngest_valid_age(data):
    """Find the youngest billionaire with a valid age."""
    curr = data[0]
    for person in data:
        if person['age'] > 0 and person['age'] < curr['age']:
            curr = person
    return curr
result = forbes_find_youngest_valid_age(data)
print(result)
