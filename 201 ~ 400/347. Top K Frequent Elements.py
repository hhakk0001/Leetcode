"""251121"""

from collections import defaultdict
from typing import List
from collections import Counter
from operator import itemgetter
import heapq


# FT
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    nums_dict = defaultdict(int)
    res = []

    # 統計出現次數
    for n in nums:
        nums_dict[n] += 1

    # 取出前 k 大頻率的元素
    for _ in range(k):
        max_num = max(nums_dict, key=nums_dict.get)
        res.append(max_num)
        nums_dict.pop(max_num)

    return res


# Heap
def topKFrequent(nums, k):
    freq_map = Counter(nums)  # 統計頻率
    top_k = heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])

    res = []
    for item in top_k:
        res.append(item[0])

    return res


# Bucket Sort
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    nums_freq = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in nums_freq.items():
        bucket[freq].append(num)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res


# k-v pair sort
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 用 Counter 統計頻率並轉成 tuple，直接做排序
    items = sorted(Counter(nums).items(), key=itemgetter(1), reverse=True)
    return [x[0] for x in items[:k]]
