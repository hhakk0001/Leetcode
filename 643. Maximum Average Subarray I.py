"""251203"""

from typing import List


# FT: Sliding Window
def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    # sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # slide the window
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum / k


# BF
def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    max_avg = float("-inf")  # 初始化為最小值

    for i in range(n - k + 1):  # 每個可能的起始位置
        window_sum = 0
        for j in range(i, i + k):  # 計算長度為 k 的子陣列總和
            window_sum += nums[j]
        avg = window_sum / k
        max_avg = max(max_avg, avg)

    return max_avg
