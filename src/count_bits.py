""" Implemntation of the Bit Counting Kata. """
def countBits(n):
    """ Converts a number to binary and counts the number of 1 bits. """
    print(n)
    val = bin(n)
    print(val)
    return val.count("1")
