"""251126"""

import sys


# FT:
def smallestRepunitDivByK(self, k: int) -> int:
    n = 1
    remainders_freq = {}

    while True:
        remainder = n % k
        if remainder == 0:
            sys.set_int_max_str_digits(0)
            return len(str(n))
        elif remainder in remainders_freq:
            return -1
        else:
            remainders_freq[remainder] = 1

        n = n * 10 + 1


# Modified
def smallestRepunitDivByK(self, k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1

    remainder = 1 % k
    for i in range(1, k + 1):
        if remainder == 0:
            return i
        remainder = (10 * remainder + 1) % k
