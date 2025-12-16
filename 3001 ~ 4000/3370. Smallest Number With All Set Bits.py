"""251029"""


# FT:
class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 1

        while res - 1 < n:
            res *= 2

        return res - 1


# Using bit_length()
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
