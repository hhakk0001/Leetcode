"""251028"""


# FT
def countValidSelections(self, nums: list[int]) -> int:
    valid_count = 0

    for idx in range(len(nums)):
        if nums[idx] == 0:
            left_sum = sum(nums[0:idx])
            right_sum = sum(nums[idx + 1 :])
            if left_sum == right_sum:
                valid_count += 2
            elif abs(left_sum - right_sum) == 1:
                valid_count += 1

    return valid_count


# Prefix Sum
def countValidSelections(self, nums: list[int]) -> int:
    # 計算好總和，並在走訪陣列時同步更新前綴和
    total_sum = sum(nums)
    left_sum = 0
    valid_count = 0

    for n in nums:
        if n == 0:
            right_sum = total_sum - left_sum
            if left_sum == right_sum:
                valid_count += 2
            elif abs(left_sum - right_sum) == 1:
                valid_count += 1
        left_sum += n  # 更新前綴和

    return valid_count
