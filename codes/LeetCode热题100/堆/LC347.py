"""
思路：
定义哈希表 cnt 维护每个元素的出现次数；定义最小堆 hp 维护前 k 个出现次数最多的元素。
遍历哈希表每个键值对并加入最小堆，如果堆中元素数量超过 k，则弹出堆顶元素。
"""

from collections import Counter
import heapq
from typing import List


class Solution347:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cnt = Counter(nums)
        hp = []
        for key, val in cnt.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        for x in hp:
            ans.append(x[1])
        return ans
