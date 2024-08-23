"""
思路：
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示前 i 个房子能偷到的最大金额。
b.状态转移方程
站在选还是不选的角度，
如果选第 i 个房子，则第 i-1 个房子不能偷，只能偷第 i-2 个房子；
如果不选第 i 个房子，则第 i-1 个房子必须偷；
两者取最大值即可，即 dfs(i) = max(dfs(i-1), dfs(i-2) + nums[i])；
c.初始状态
dfs(0...n-1) = 0，表示刚开始没偷到任何房子的钱。
d.答案
dfs(n-1)，表示从前 n-1 个房子能偷到的最大金额。
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = max(dfs(i-1), dfs(i-2) + nums[i]) => dp[i+2] = max(dp[i+1], dp[i] + nums[i])
dfs(0...n-1) = 0 => dp = [0] * (n+2)
dfs(n-1) => dp[-1]
"""

from functools import cache
from typing import List


class Solution198:
    def rob(self, nums: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i - 1), dfs(i - 2) + nums[i])
        #
        # n = len(nums)
        # return dfs(n - 1)

        # n = len(nums)
        # dp = [0] * (n + 2)
        # for i in range(n):
        #     dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        # return dp[-1]

        f0 = f1 = 0
        for x in nums:
            new_f = max(f1, f0 + x)
            f0 = f1
            f1 = new_f
        return f1
