"""251221"""

from typing import List


# FT: Greedy
def minDeletionSize(self, strs: List[str]) -> int:
    n, m = len(strs), len(strs[0])
    res_strs = [""] * n  # 最後得到的陣列
    res = 0

    for col in range(m):  # 檢查每一欄的字母
        for row in range(n - 1):  # 比較相鄰字串
            # 如果加上該欄位字母無法保持字典序，則不加入(即刪除該欄位)
            if res_strs[row] + strs[row][col] > res_strs[row + 1] + strs[row + 1][col]:
                res += 1
                break
        else:  # 若所有字串的該欄位都維持字典序，直接保留整欄
            for i in range(n):
                res_strs[i] += strs[i][col]
    return res


# Greedy with Optimization
def minDeletionSize(self, strs: List[str]) -> int:
    n, m = len(strs), len(strs[0])
    check_list = list(range(n - 1))  # 紀錄需要比較的相鄰字串
    res = 0

    for col in range(m):
        for row in check_list:
            if strs[row][col] > strs[row + 1][col]:
                # 不符合字典序，刪除欄位
                res += 1
                break
        else:
            # 該欄位上字串皆符合字典序
            new_size = 0

            for row in check_list:
                if strs[row][col] == strs[row + 1][col]:
                    # 相鄰字串的欄位字母相同，繼續往下一欄比較
                    check_list[new_size] = row  # 原地覆蓋，保留仍需比較的字串
                    new_size += 1
            del check_list[new_size:]  # 刪除舊的資料

    return res
