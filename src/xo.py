"""This is an implmentation of the Exes and Ohs kata."""


def xo(s):
    """Determine if the string has the same number of x's and o's."""
    s = s.lower()
    x_count = s.count('x')
    o_count = s.count('o')

    return x_count == o_count
