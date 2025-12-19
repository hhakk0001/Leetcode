"""2512XX"""

from typing import List


# DP + Prefix & Suffix
def trap(self, height: List[int]) -> int:
    n = len(height)

    # 計算前綴最大值陣列
    pre_max = [0] * n
    pre_max[0] = height[0]
    for i in range(1, n):
        pre_max[i] = max(pre_max[i - 1], height[i])

    # 計算後綴最大值陣列
    suf_max = [0] * n
    suf_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        suf_max[i] = max(suf_max[i + 1], height[i])

    # 遍歷計算容量
    ans = 0
    for h, pre, suf in zip(height, pre_max, suf_max):
        ans += min(pre, suf) - h

    return ans


# Two Pointers
def trap(self, height: List[int]) -> int:
    ans = pre_max = suf_max = 0
    left, right = 0, len(height) - 1
    while left < right:
        pre_max = max(pre_max, height[left])
        suf_max = max(suf_max, height[right])
        if pre_max < suf_max:
            ans += pre_max - height[left]
            left += 1
        else:
            ans += suf_max - height[right]
            right -= 1
    return ans
