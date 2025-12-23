"""251223"""

from typing import List


# FT: SW
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    left = 0
    p = 1
    res = 0

    # 陣列元素必為正整數
    if k <= 1:
        return 0

    for right, num in enumerate(nums):
        p *= num
        while p >= k:
            p /= nums[left]
            left += 1
        res += right - left + 1  # 以 right 為右邊界會產生的子陣列數量
    return res
