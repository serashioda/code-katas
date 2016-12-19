"""Implementation of the Sum of the first nth term of Series Kata."""


def series_sum(n):
    """Return the sum of series in range."""
    return "%.2f" % sum((1.0 / (3 * i + 1) for i in range(n)))
