Repo containing my solutions from Code War katas.

###8kyu

####Multiply:
- MODULE: multiply.py
- TESTS: test_sum_multiply.py
- LINK:
- Interesting solution by ____:
- """

- """

###7kyu


###Decending Order:
- MODULE: decending_order.py
- TESTS: test_decending_order.py
- LINK:
- Interesting solution by Edwin.01:
- """ def Descending_Order(num):
-    return int(''.join(str(x) for x in sorted(str(num))[::-1]))
- """


###Remove the Minimum:
- MODULE: ______.py
- TESTS: test____________.py
- LINK:
- Interesting solution by _____:
- """

- """


###Money, Money, Money:
- MODULE: .py
- TESTS: test____________.py
- LINK:
- Interesting solution by CrazyMerlyn:
- """
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0

    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
- """


###Isograms:
- MODULE: is_isogram.py
- TESTS: test_is_isogram.py
- LINK:
- Interesting solution by madbook, Kamyk, hiasen, dia_c, staticor, lancelote (plus 76 more warriors):
- """
def is_isogram(string):
    return len(string) == len(set(string.lower()))
- """


###Exes and Ohs:
- MODULE: xo.py
- TESTS: test_xo.py
- LINK: https://www.codewars.com/kata/exes-and-ohs
- Interesting solution by jolaf, Beast, Tgc, MMMAAANNN, SquishyStrawberry, Devilart (plus 126 more warriors):
- """
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
- """


###Shortest Word:
- MODULE: shortest_word.py
- TESTS: test_shortest_word.py
- LINK: https://www.codewars.com/kata/shortest-word
- Interesting solution by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 (plus 12 more warriors):
- """
def find_short(s):
    return min(len(x) for x in s.split())

- """


###6kyu

###Find the Odd Int:
- MODULE: ______.py
- TESTS: test____________.py
- LINK:
- Interesting solution by Unnamed:
- """
import operator

def find_it(xs):
    return reduce(operator.xor, xs)
- """


###Bit Counting:
- MODULE: count_bits.py
- TESTS: test_count_bits.py
- LINK: https://www.codewars.com/kata/bit-counting
- Interesting solution by NTERESTING
xcthulhu, hiasen, RM84, mpeddle, nickie, npd (plus 361 more warriors):
- """
def countBits(n):
    return bin(n).count("1")
- """
