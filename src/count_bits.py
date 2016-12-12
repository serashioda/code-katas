"""Implementation of the Bit Counting Kata."""


def count_bits(n):
    """Convert a number to binary and counts the number of 1 bits."""
    print(n)
    val = bin(n)
    print(val)
    return val.count("1")
