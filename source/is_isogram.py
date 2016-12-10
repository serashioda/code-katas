""" Implementation of the Kata Isograms. """
def is_isogram(string):
    """ This tells you if a string is a isogram, word that has no repeating letters. """

    string = string.lower()

    if len(string) == 0:
        return True

    for letter in string:
        if string.count(letter) > 1:
            return False

    return True
