"""251214"""

from typing import List


# FT: SW
def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    n = len(arr)
    window_sum = sum(arr[:k])
    res = 0

    if window_sum >= threshold * k:
        res += 1

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum >= threshold * k:
            res += 1

    return res
