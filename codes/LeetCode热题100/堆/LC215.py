"""
思路：
本题属于典型的 TopK 问题，可以使用堆解决。
具体做法是定义最小堆维护前 K 个最大元素，每次将数组元素加入堆中，如果堆大小不小于 k，则弹出堆顶元素。
"""

import heapq
from typing import List


class Solution215:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for i, x in enumerate(nums):
            heapq.heappush(hp, x)
            if i >= k:
                heapq.heappop(hp)
        return hp[0]
