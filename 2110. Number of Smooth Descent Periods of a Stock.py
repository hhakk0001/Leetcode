"""251215"""

from typing import List


# DP
def getDescentPeriods(self, prices: List[int]) -> int:
    res = 1  # 初始 prices[0] 自行構成一個 SDP
    prev = 1  # 以 prices[i-1] 結尾的 SDP 長度

    for i in range(1, len(prices)):
        if prices[i] == prices[i - 1] - 1:  # 若符合條件，增加 SDP 長度
            prev += 1
        else:  # SDP 未繼續增長，長度重設為 1
            prev = 1
        res += prev

    return res
