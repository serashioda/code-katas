""" Finds an integer apparing an odd number of times. """

def find_it(seq):
    """ returns only number appearing odd number of times. """
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
