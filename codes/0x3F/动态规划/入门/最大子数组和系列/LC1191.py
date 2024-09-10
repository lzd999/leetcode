"""
思路：
由题意可知 k ∈ [1, 10^5]，如果 k = 1，相当于就是 LC53.最大子数组和，
如果 k >= 2，定义 s 为数组 nums 的所有元素之和，则有如下两种情况：
1.数组的全部元素都是负数，即 s < 0，那么最大子数组和只会是 0，因为数组重复次数越多，子数组和反而越小。
2.数组的全部元素都是正数，即 s > 0，那么最大子数组和就是整个数组的和重复 k 次后的结果。
3.数组的部分元素为正数，部分元素为负数，那么最大子数组和就是数组正数部分重复 k 次后的结果。
"""

from functools import cache
from math import inf
from typing import List


class Solution1191:
    def kConcatenationMaxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        s = sum(nums)
        if k == 1:
            return max(0, self.maxSubArray(nums)) % MOD
        else:
            return max(0, self.maxSubArray(nums * 2) + max(0, (k - 2) * s)) % MOD

    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), 0) + nums[i]

        n = len(nums)
        res = -inf
        for i in range(n):
            res = max(res, dfs(i))
        return res
