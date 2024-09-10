"""
思路：
核心思路仍是参考 LC53.最大子数组和，本题与 LC53 的区别在于，
环形整数数组需要额外考虑取到首尾元素组成子数组的情况。
如果子数组在 nums 内选取，没有选取首尾的情况，则等价于 LC53；
如果子数组选取了 nums 的首尾元素，由于 子数组和 + 剩余元素和 = 整个数组和，因此剩余元素和越小，子数组和越大，
如果换个角度讲剩余元素视为子数组，则可计算最小子数组和，然后与整个数组和相减，就得到了选取首尾元素的子数组的最大和；
※ 还可能有一种情况，即最小子数组为整个数组，这种情况的判断依据是【最小子数组和与整个数组和相等】。
1.记忆化搜索
a.状态定义
定义 dfs_max(i) 表示以 nums[i] 结尾的最大子数组和；
定义 dfs_min(i) 表示以 nums[i] 结尾的最小子数组和；
b.状态转移方程
由分析可知，
最大子数组和 max_s = max(dfs_max(i), 0)
最小子数组和 min_s = min(dfs_min(i), 0)
c.初始状态
最大子数组和 max_s = -inf，因为最大子数组和不能为空；
最小子数组和 min_s = 0，因为最小子数组和可以为空；
d.答案
如果 min_s 与 s = sum(nums) 相等，则返回 max_s，否则返回 max(max_s, s - min_s)
2.1:1翻译成递推
dfs_max(i) => dp_max[i]
dfs_min(i) => dp_min[i]
max_s = max(dfs_max(i), 0) => max_s = max(dp_max[i], 0) + nums[i]
min_s = min(dfs_min(i), 0) => min_s = min(dp_min[i], 0) + nums[i]
"""

from functools import cache
from math import inf
from typing import List


class Solution918:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
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
        # max_s = -inf
        # min_s = inf
        # s = sum(nums)
        # for i in range(n):
        #     max_s = max(max_s, dfs_max(i))
        #     min_s = min(min_s, dfs_min(i))
        #
        # if min_s == s:
        #     return max_s
        # return max(max_s, s - min_s)

        # n = len(nums)
        # s = sum(nums)
        # max_s, min_s = -inf, inf
        # dp_max = [0] * (n + 1)
        # dp_min = [0] * (n + 1)
        # for i, x in enumerate(nums):
        #     dp_max[i + 1] = max(dp_max[i], 0) + x
        #     max_s = max(max_s, dp_max[i + 1])
        #     dp_min[i + 1] = min(dp_min[i], 0) + x
        #     min_s = min(min_s, dp_min[i + 1])
        # if min_s == s:
        #     return max_s
        # return max(max_s, s - min_s)

        s = sum(nums)
        max_s, min_s = -inf, inf
        dp_max = dp_min = 0
        for x in nums:
            dp_max = max(dp_max, 0) + x
            max_s = max(max_s, dp_max)
            dp_min = min(dp_min, 0) + x
            min_s = min(min_s, dp_min)
        if min_s == s:
            return max_s
        return max(max_s, s - min_s)
