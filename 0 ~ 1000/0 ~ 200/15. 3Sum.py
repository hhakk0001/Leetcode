"""251216"""

from typing import List


# Two Pointers 1
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    n = len(nums)

    # i < j < k
    # 列舉 i，找 j, k 所指兩數之和為 -nums[i] 者
    for i in range(n - 2):  # 至少要留兩個給 j , k
        i_value = nums[i]
        if i > 0 and i_value == nums[i - 1]:  # 跳過 i 的重複值
            continue

        # 提前處理
        if i_value + nums[i + 1] + nums[i + 2] > 0:  # 最小的三元組還太大，則無符合可能
            break
        if (
            i_value + nums[-2] + nums[-1] < 0
        ):  # 當前的 i 可構成的最大三元組仍不夠，直接找下一組
            continue

        # 求已排序中的兩數之和
        j, k = i + 1, n - 1
        while j < k:
            tri_sum = i_value + nums[j] + nums[k]
            if tri_sum > 0:
                k -= 1
            elif tri_sum < 0:
                j += 1
            else:
                ans.append([i_value, nums[j], nums[k]])

                # 跳過 j, k 的重複值
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                k -= 1
                while j < k and nums[k] == nums[k + 1]:  # k 是由右至左，不會越界
                    k -= 1
    return ans


# Two Pointers 2
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    n = len(nums)

    # i < j < k
    # 列舉 i，找 j, k 所指兩數之和為 -nums[i] 者
    for i in range(n - 2):  # 至少要留兩個給 j , k
        i_value = nums[i]
        if i > 0 and i_value == nums[i - 1]:  # 跳過 i 的重複值
            continue

        # 提前處理
        if i_value + nums[i + 1] + nums[i + 2] > 0:  # 最小的三元組還太大，則無符合可能
            break
        if (
            i_value + nums[-2] + nums[-1] < 0
        ):  # 當前的 i 可構成的最大三元組仍不夠，直接找下一組
            continue

        # 求已排序中的兩數之和
        j, k = i + 1, n - 1
        while j < k:
            tri_sum = i_value + nums[j] + nums[k]
            if tri_sum > 0:
                k -= 1
            elif tri_sum < 0:
                j += 1
            else:
                # 跳過 j, k 的重複值
                if j == i + 1 or nums[j] != nums[j - 1]:
                    ans.append([i_value, nums[j], nums[k]])
                j += 1
                k -= 1
    return ans
