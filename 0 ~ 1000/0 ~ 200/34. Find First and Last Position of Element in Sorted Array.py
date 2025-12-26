"""251225"""

from typing import List


# FT
def lower_bound(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def searchRange(self, nums: List[int], target: int) -> List[int]:
    start = self.lower_bound(nums, target)

    # 如果整個陣列都小於 target 或 target 不存在
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    end = self.lower_bound(nums, target + 1) - 1
    return [start, end]
