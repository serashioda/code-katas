"""Implementation of the Kata Remove the Minimum."""

def remove_smallest(numbers):
    """takes an array of integers and remove one of the smallest numbers(s). """
    try:
        numbers.remove(min(numbers))
    except ValueError:
        pass
    return numbers
