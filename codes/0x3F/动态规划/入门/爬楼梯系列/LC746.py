"""
思路：
本题在 LC70.爬楼梯 的基础上，附带了爬每一阶楼梯的花费 cost，
最终要求的也并非是方法数而是最小花费。
因此可以在 LC70.爬楼梯 的基础上，将原本求方法数的步骤修改为求最小花费的步骤即可。
"""

from typing import List


class Solution746:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i <= 1:
        #         return 0
        #     return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
        #
        # n = len(cost)
        # return dfs(n)

        # n = len(cost)
        # dp = [0] * (n + 1)
        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[-1]

        n = len(cost)
        f0 = f1 = 0
        for i in range(2, n + 1):
            new_f = min(f1 + cost[i - 1], f0 + cost[i - 2])
            f0 = f1
            f1 = new_f
        return f1
