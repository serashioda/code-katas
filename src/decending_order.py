"""Implementation of the Kata Descending_Order."""


def Descending_Order(num):
    """takes a non-neg integer and returns its digits in decending order. """
    num_array = list(str(num))
    reverse_array = sorted(num_array, reverse=True)
    reverse_string = ''.join(reverse_array)
    reverse_num = int(reverse_string)
    return reverse_num
