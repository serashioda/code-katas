Repo containing my solutions from Code Katas.

###8kyu

####Multiply:
- MODULE: multiply.py
- TESTS: test_multiply.py
- LINKS: 
[Multiply - Kata](https://www.codewars.com/kata/multiply/train/python);
[Solutions](https://www.codewars.com/kata/50654ddff44f800200000004/solutions/python/me/best_practice)
- Interesting solution by jihygk:
```
multiply = __import__('operator').mul
```

###7kyu


####Decending Order:
- MODULE: decending_order.py
- TESTS: test_decending_order.py
- LINKS: 
[Decending Order - Kata](https://www.codewars.com/kata/descending-order/train/python);
[Solutions](https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python/me/best_practice)
- Interesting solution by Edwin.01:
```
def Descending_Order(num):
   return int(''.join(str(x) for x in sorted(str(num))[::-1]))
```


####Remove the Minimum:
- MODULE: remove_min.py
- TESTS: test_remove.min.py
- LINKS: 
[Remove the Minimum - Kata](https://www.codewars.com/kata/remove-the-minimum/train/python);
[Solutions](https://www.codewars.com/kata/563cf89eb4747c5fb100001b/solutions/python/me/best_practice)
- Interesting solution by Streetmentioner, Emigre, syim, JustyFY, MMMAAANNN, doublenns (plus 94 more warriors):
```
def remove_smallest(numbers):
   if numbers:
       numbers.remove(min(numbers))
    return numbers
```


####Money, Money, Money:
- MODULE: calculate_years.py
- TESTS: test_calculate_years.py
- LINKS: 
[Money, Money, Money - Kata](https://www.codewars.com/kata/money-money-money/train/python);
[Solutions](https://www.codewars.com/kata/563f037412e5ada593000114/solutions/python/me/best_practice)
- Interesting solution by CrazyMerlyn:
```
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
  if principal >= desired: return 0

  return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
```


####Isograms:
- MODULE: is_isogram.py
- TESTS: test_is_isogram.py
- LINKS: 
[Isograms - Kata](https://www.codewars.com/kata/isograms/train/python);
[Solutions](https://www.codewars.com/kata/54ba84be607a92aa900000f1/solutions/python/me/best_practice)
- Interesting solution by madbook, Kamyk, hiasen, dia_c, staticor, lancelote (plus 76 more warriors):
```
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```


####Exes and Ohs:
- MODULE: xo.py
- TESTS: test_xo.py
- LINKS: 
[Exes and Ohs - Kata](https://www.codewars.com/kata/exes-and-ohs/train/python);
[Solutions](https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python/me/best_practice)
- Interesting solution by jolaf, Beast, Tgc, MMMAAANNN, SquishyStrawberry, Devilart (plus 126 more warriors):
```
def xo(s):
  s = s.lower()
    return s.count('x') == s.count('o')
```


####Shortest Word:
- MODULE: shortest_word.py
- TESTS: test_shortest_word.py
- LINKS: 
[Shortest Word - Kata](https://www.codewars.com/kata/shortest-word/train/python);
[Solutions](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python/me/best_practice)
- Interesting solution by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 (plus 12 more warriors):
```
def find_short(s):
  return min(len(x) for x in s.split())
```


###6kyu


####Find the Odd Int:
- MODULE: find_odd_int.py
- TESTS: test_find_odd_int.py
- LINKS: 
[Find the Odd Int - Kata](https://www.codewars.com/kata/find-the-odd-int/train/python);
[Solutions](https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/python/me/best_practice)
- Interesting solution by Unnamed:
```
import operator

def find_it(xs):
  return reduce(operator.xor, xs)
```


####Bit Counting:
- MODULE: count_bits.py
- TESTS: test_count_bits.py
- LINKS: [Bit Counting - Kata](https://www.codewars.com/kata/bit-counting/train/python),
[Solutions](https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/python/me/best_practice)
- Interesting solution by NTERESTING, xcthulhu, hiasen, RM84, mpeddle, nickie, npd (plus 361 more warriors):
```
def countBits(n):
  return bin(n).count("1")
```


###Other


####Interview Challenge: Proper Parenthetics
- Module: proper-parenthetics.py
- TESTS: test_proper-parenthetics.py
- LINKS: None.
- DERIVED FROM: [data-structures repo. Specifically stack branch](https://github.com/ellezv/data_structures/tree/stack), collaborated with Maelle Vance.


####Autocomplete
- Module: autocomplete.py
- TESTS: test_autocomplete.py
- LINKS: None.


###COVERAGE

```

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
src/autocomplete.py                    13      0   100%
src/calculate_years.py                  8      0   100%
src/count_bits.py                       5      0   100%
src/decending_order.py                  6      6     0%   4-10
src/find_odd_int.py                     4      0   100%
src/is_isogram.py                       8      0   100%
src/multiply.py                         2      0   100%
src/parenthetics.py                    48      0   100%
src/remove_min.py                       6      0   100%
src/shortest_word.py                    7      0   100%
src/sort_cards.py                      34     13    62%   11-12, 22, 28-32, 36-38, 51-52
src/sum_terms.py                        2      0   100%
src/tests/__init__.py                   0      0   100%
src/tests/test_autocomplete.py          7      0   100%
src/tests/test_calculate_years.py       5      0   100%
src/tests/test_count_bits.py            5      0   100%
src/tests/test_decending_order.py       5      2    60%   16-17
src/tests/test_find_odd_int.py          5      0   100%
src/tests/test_is_isogram.py            5      0   100%
src/tests/test_multiply.py              5      0   100%
src/tests/test_parenthetics.py         12      0   100%
src/tests/test_remove_min.py            5      0   100%
src/tests/test_shortest_word.py         5      0   100%
src/tests/test_sort_cards.py            7      0   100%
src/tests/test_sum_terms.py             5      0   100%
src/tests/test_xo.py                    5      0   100%
src/xo.py                               5      0   100%
-----------------------------------------------------------------
TOTAL                                 224     21    91%


===================== 45 passed in 0.38 seconds =====================
```



