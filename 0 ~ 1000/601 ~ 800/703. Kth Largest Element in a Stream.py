"""251027"""

import heapq


# FT: Heap(using heapq)
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # 以堆積的方式紀錄最大值
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # 若初始堆積超過 k，縮小到 k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # 插入新值
        heapq.heappush(self.min_heap, val)

        # 維持堆積的大小為 k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # 堆積頂部即為第 k 大
        return self.min_heap[0]


# Sorting
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)

        # 每次插入新元素時重新排序
        self.arr.sort()

        return self.arr[len(self.arr) - self.k]
