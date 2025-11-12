"""251112"""

from typing import List


# FT: Iteration
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize the upper and lower boundaries
        left, right = 0, len(nums) - 1

        # loop as long as the search space is valid
        while left <= right:
            # equals to mid = (left + right) // 2 in Python
            # this form prevents potential overflow in other languages
            mid = left + (right - left) // 2

            # Narrow down the search space based on comparison
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        # if target not found in array
        return -1


# Recursion
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left: int, right: int) -> int:
            # Base case: invalid search range
            if left > right:
                return -1

            mid = left + (right - left) // 2

            # Compare mid value with target
            if nums[mid] < target:
                # Search in the right half
                return bs(mid + 1, right)
            elif nums[mid] > target:
                # Search in the left half
                return bs(left, mid - 1)
            else:
                # Found the target
                return mid

        # Initiate recursive search in full range
        return bs(0, len(nums) - 1)
