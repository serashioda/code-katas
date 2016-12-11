Repo containing my solutions from Code War katas.

###8kyu

####Multiply:
- MODULE: multiply.py
- TESTS: test_multiply.py
- LINK: https://www.codewars.com/kata/multiply/train/python
- https://www.codewars.com/kata/50654ddff44f800200000004/solutions/python/me/best_practice
- Interesting solution by jihygk:
```
multiply = __import__('operator').mul
```

###7kyu


###Decending Order:
- MODULE: decending_order.py
- TESTS: test_decending_order.py
- LINK: https://www.codewars.com/kata/descending-order/train/python
- https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python/me/best_practice
- Interesting solution by Edwin.01:
```
def Descending_Order(num):
   return int(''.join(str(x) for x in sorted(str(num))[::-1]))
```


###Remove the Minimum:
- MODULE: remove_min.py
- TESTS: test_remove.min.py
- LINK: https://www.codewars.com/kata/remove-the-minimum/train/python
- https://www.codewars.com/kata/563cf89eb4747c5fb100001b/solutions/python/me/best_practice
- Interesting solution by Streetmentioner, Emigre, syim, JustyFY, MMMAAANNN, doublenns (plus 94 more warriors):
```
def remove_smallest(numbers):
   if numbers:
       numbers.remove(min(numbers))
    return numbers
```


###Money, Money, Money:
- MODULE: calculate_years.py
- TESTS: test_calculate_years.py
- LINK: https://www.codewars.com/kata/money-money-money/train/python
- https://www.codewars.com/kata/563f037412e5ada593000114/solutions/python/me/best_practice
- Interesting solution by CrazyMerlyn:
```
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
  if principal >= desired: return 0

  return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
```


###Isograms:
- MODULE: is_isogram.py
- TESTS: test_is_isogram.py
- LINK: https://www.codewars.com/kata/isograms/train/python
- https://www.codewars.com/kata/54ba84be607a92aa900000f1/solutions/python/me/best_practice
- Interesting solution by madbook, Kamyk, hiasen, dia_c, staticor, lancelote (plus 76 more warriors):
```
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```


###Exes and Ohs:
- MODULE: xo.py
- TESTS: test_xo.py
- LINK: https://www.codewars.com/kata/exes-and-ohs/train/python
- https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python/me/best_practice
- Interesting solution by jolaf, Beast, Tgc, MMMAAANNN, SquishyStrawberry, Devilart (plus 126 more warriors):
```
def xo(s):
  s = s.lower()
    return s.count('x') == s.count('o')
```


###Shortest Word:
- MODULE: shortest_word.py
- TESTS: test_shortest_word.py
- LINK: https://www.codewars.com/kata/shortest-word/train/python
- https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python/me/best_practice
- Interesting solution by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 (plus 12 more warriors):
```
def find_short(s):
  return min(len(x) for x in s.split())
```


###6kyu


###Find the Odd Int:
- MODULE: find_odd_int.py
- TESTS: test_find_odd_int.py
- LINK: https://www.codewars.com/kata/find-the-odd-int/train/python
- https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/python/me/best_practice
- Interesting solution by Unnamed:
```
import operator

def find_it(xs):
  return reduce(operator.xor, xs)
```


###Bit Counting:
- MODULE: count_bits.py
- TESTS: test_count_bits.py
- LINK: https://www.codewars.com/kata/bit-counting/train/python
- https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/python/me/best_practice
- Interesting solution by NTERESTING, xcthulhu, hiasen, RM84, mpeddle, nickie, npd (plus 361 more warriors):
```
def countBits(n):
  return bin(n).count("1")
```
