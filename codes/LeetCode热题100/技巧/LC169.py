"""
思路：
根据题目对多数元素的定义，很容易能想到：
1.使用哈希表维护每个元素的出现次数，然后遍历哈希表，出现次数大于 n // 2 的元素即为多数元素；
2.对数组排序，位于排序后数组中间位置的元素即为多数元素。
但第一个方法的空间复杂度为 O(n)，第二个方法的时间复杂度为 O(nlogn)，不符合题目要求。
这里介绍一个新方法：摩尔投票，该算法的核心思想是每个数组元素票数的正负抵消，
如果一个数组元素为多数元素，那么它到最后的票数一定不为 0。
"""

from collections import Counter
from typing import List


class Solution169:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        most = nums[0]
        for x in nums:
            if most == x:
                votes += 1
                continue
            if votes == 0:
                most = x
                votes += 1
                continue
            votes -= 1
        return most

        # return sorted(nums)[len(nums) // 2]

        # n = len(nums)
        # cnt = Counter(nums)
        # for k, v in cnt.items():
        #     if v > n // 2:
        #         return k
