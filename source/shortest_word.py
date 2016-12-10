""" Implementation of the Shortest Word Kata. """


def find_short(s):
    """ returns the shortest word our of a string of words. """
    shortest = 999999999

    words = s.split(' ')

    for word in words:
        if shortest > len(word):
            shortest = len(word)

    return shortest
