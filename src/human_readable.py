"""Implementation of the human readable module - 5 kyu"""

"""
Human Readable Time

1661985% of 7472,589 of 9,280BattleRattle8 Issues Reported
Python
2.7.6
VIM
EMACS
Instructions
Output
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(seconds):