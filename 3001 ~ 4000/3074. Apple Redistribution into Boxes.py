"""251224"""

from typing import List


# FT: Greedy
def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    apples = sum(apple)
    capacity.sort(reverse=True)

    box_selected = 0
    while apples > 0:
        apples -= capacity[box_selected]
        box_selected += 1

    return box_selected
