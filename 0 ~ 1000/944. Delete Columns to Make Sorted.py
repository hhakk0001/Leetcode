"""251220"""

from typing import List


# FT: BF
def minDeletionSize(self, strs: List[str]) -> int:
    n, m = len(strs), len(strs[0])
    res = 0

    for col in range(m):
        for row in range(n - 1):
            if strs[row][col] > strs[row + 1][col]:
                res += 1
                break
    return res
