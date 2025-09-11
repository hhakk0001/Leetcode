# 暴力法
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Two-pass Hash Table: 建立字典後進行查詢
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 將列表內容以字典形式儲存
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i

    # 以字典形式查看是否存在總和為目標值的目標
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_dict and nums_dict[complement] != i:
            return [i, nums_dict[complement]]


# One-pass Hash Table: 邊建立字典邊查詢
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 將列表內容以字典形式儲存
    nums_dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_dict:
            return [i, nums_dict[complement]]
        nums_dict[nums[i]] = i
