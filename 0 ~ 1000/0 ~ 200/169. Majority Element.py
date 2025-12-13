"""250910"""


# 雜湊表解
def majorityElement(self, nums: list[int]) -> int:
    # 以字典形式儲存列表中的數字與出現次數
    nums_dict = {}

    # 如果數字出現過就增加次數
    for n in nums:
        if n in nums_dict:
            nums_dict[n] += 1
        else:
            nums_dict[n] = 1

    # 找到出現次數過半的數字
    for n, times in nums_dict.items():
        if times >= (len(nums) / 2):
            return n


# 排序後取中位數
def majorityElement(self, nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]


# 摩爾投票法
def majorityElement(self, nums: list[int]) -> int:
    candidate = None
    count = 0

    for n in nums:
        if count == 0:
            candidate = n

        if n == candidate:
            count += 1
        else:
            count -= 1

    return candidate
