"""
思路：
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示以 nums[i] 结尾的连续子数组的最大和。
b.状态转移方程
由于数组中存在负数，和可能会变小，因此要分情况：
如果 nums[i] 单独成为一个子数组，说明 dfs(i-1) < 0，dfs(i) = nums[i]。
如果 nums[i] 能和 dfs(i-1) 构成更长的子数组，说明 dfs(i-1) > 0，dfs(i) = dfs(i-1) + nums[i]。
两种情况取最大值即可。
c.初始状态
dfs(0) = nums[0]，表示以 nums[0] 结尾的子数组和为 nums[0] 本身。
d.答案
max(dfs(i))
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = max(dfs(i-1), 0) + nums[i] => dp[i] = max(dp[i-1], 0) + nums[i]
dfs(0) = nums[0] => dp[0] = nums[0]
max(dfs(i)) => max(dp[i])
"""

from functools import cache
from math import inf
from typing import List


class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return nums[0]
        #     return max(dfs(i - 1), 0) + nums[i]
        #
        # n = len(nums)
        # ans = -inf
        # for i in range(n):
        #     ans = max(ans, dfs(i))
        # return ans

        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1], 0) + nums[i]
        # return max(dp)

        ans = -inf
        dp = 0
        for x in nums:
            dp = max(dp, 0) + x
            ans = max(ans, dp)
        return ans
