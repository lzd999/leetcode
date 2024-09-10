"""
思路：
由题意可知，本题可转化为 LC53.最大子数组和 与 最小子数组和的相反数 里取最大值
1.记忆化搜索
a.状态定义
定义 dfs_max(i) 表示以 nums[i] 结尾的最大子数组和
定义 dfs_min(i) 表示以 nums[i] 结尾的最小子数组和
b.状态转移方程
如果 nums[i] 为正整数，则 dfs_max(i) = max(dfs_max(i-1), 0) + nums[i]；
如果 nums[i] 为负整数，则 dfs_min(i) = min(dfs_min(i-1), 0) + nums[i]；
取最大值即可 max(dfs_max(i), -dfs_min(i))。
c.初始状态
dfs_max(0) = dfs_min(0) = 0，表示空数组和为 0
d.答案
max(dfs_max(i), -dfs_min(i)) i ∈ [0, n-1]
2.1:1翻译成递推
dfs_max(i) => dp_max[i]
dfs_min(i) => dp_min[i]
dfs_max(i) = max(dfs_max(i-1), 0) + nums[i] => dp_max[i] = max(dp_max[i-1], 0) + nums[i]
dfs_min(i) = min(dfs_min(i-1), 0) + nums[i] => dp_min[i] = min(dp_min[i-1], 0) + nums[i]
max(dfs_max(i), -dfs_min(i)) => max(dp_max[i], -dp_min[i])
dfs_max(0) = dfs_min(0) = 0 => dp_max[0] = dp_min[0] = 0
max(dfs_max(i), -dfs_min(i)) i ∈ [0, n-1] => max(dp_max[i], dp_min[i]) i ∈ [0, n-1]
"""

from functools import cache
from math import inf
from typing import List


class Solution1749:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # @cache
        # def dfs_max(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs_max(i - 1), 0) + nums[i]
        #
        # @cache
        # def dfs_min(i):
        #     if i < 0:
        #         return 0
        #     return min(dfs_min(i - 1), 0) + nums[i]
        #
        # n = len(nums)
        # ans = -inf
        # for i in range(n):
        #     ans = max(ans, dfs_max(i), -dfs_min(i))
        # return ans

        # n = len(nums)
        # ans = -inf
        # dp_max = [0] * (n + 1)
        # dp_min = [0] * (n + 1)
        # for i, x in enumerate(nums):
        #     dp_max[i + 1] = max(dp_max[i], 0) + x
        #     dp_min[i + 1] = min(dp_min[i], 0) + x
        #     ans = max(ans, dp_max[i + 1], -dp_min[i + 1])
        # return ans

        ans = -inf
        dp_max = dp_min = 0
        for x in nums:
            dp_max = max(dp_max, 0) + x
            dp_min = min(dp_min, 0) + x
            ans = max(ans, dp_max, -dp_min)
        return ans
