"""
思路：
使用哈希表维护数组元素与对应下标的映射关系。
遍历数组，对每个元素 x：
a.判断 target - x 是否在哈希表，如果存在，则返回当前元素和目标元素的下标；
b.否则将当前元素及其下标存入哈希表。
"""

from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for j, x in enumerate(nums):
            if target - x in mp:
                return [mp[target - x], j]
            mp[x] = j
        return [-1, -1]
