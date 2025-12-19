"""251219"""

from typing import List


# FT: Two Pointers
def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_water = 0

    while r > l:
        water = (r - l) * min(height[l], height[r])
        max_water = max(water, max_water)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return max_water
