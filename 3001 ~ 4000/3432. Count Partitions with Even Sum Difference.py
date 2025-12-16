"""251205"""

from typing import List


# FT: Prefix Sum
def countPartitions(self, nums: List[int]) -> int:
    left_sum, right_sum = 0, sum(nums)
    ans = 0

    for x in nums[:-1]:
        left_sum += x
        right_sum -= x
        if (left_sum - right_sum) % 2 == 0:
            ans += 1

    return ans


# Math
def countPartitions(self, nums: List[int]) -> int:
    return 0 if sum(nums) % 2 else len(nums) - 1
