"""251204"""


# BF
def minChanges(self, n: int, k: int) -> int:
    ans = 0
    for i in range(20):
        bn = (n >> i) & 1
        bk = (k >> i) & 1
        if bn == 0 and bk == 1:
            return -1
        if bn != bk:
            ans += 1

    return ans


# Bitwise Operation
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # method 1
        if n & k != k:
            return -1

        return (n ^ k).bit_count()
