"""251225"""

from typing import List


# FT
def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    s = 0

    for i in range(k):
        if happiness[i] > i:
            s += happiness[i] - i

    return s
