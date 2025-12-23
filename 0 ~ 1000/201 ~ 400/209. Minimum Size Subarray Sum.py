"""251222"""

from typing import List


# FT: BF(TLE)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = n

        if sum(nums) < target:
            return 0

        # 從左開始
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s >= target:
                    min_length = min(min_length, j - i + 1)
                    break

        return min_length


# Sliding Window
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    n = len(nums)
    res = n + 1  # inf 也可
    s = 0  # 子陣列總和
    left = 0

    # 遍歷右端點
    for right, num in enumerate(nums):
        s += num
        # 如果當前總和滿足條件，則嘗試縮小陣列範圍。
        while s >= target:
            res = min(res, right - left + 1)
            s -= nums[left]
            left += 1

    if res <= n:
        return res
    else:
        return 0
