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
- MODULE: ______.py
- TESTS: test____________.py
- LINK:
- Interesting solution by CrazyMerlyn:
- """
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0

    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
- """


###6kyu Find the Odd Int:
- MODULE: ______.py
- TESTS: test____________.py
- LINK:
- Interesting solution by Unnamed:
- """
import operator

def find_it(xs):
    return reduce(operator.xor, xs)
- """
