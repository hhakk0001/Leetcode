"""251216"""

from typing import List


# FT: BF
# TLE
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]  # index starts from 1


# Two Pointers
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while True:  # left < right
        p_sum = numbers[left] + numbers[right]
        if p_sum == target:
            break
        elif p_sum < target:
            left += 1
        else:
            right -= 1
    return [left + 1, right + 1]  # index starts form 1
