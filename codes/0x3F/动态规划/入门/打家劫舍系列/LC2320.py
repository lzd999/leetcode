"""
思路：
1.记忆化搜索
a.状态定义
定义 dfs(i) 为前 i 个地块的放置房子方案数。
b.状态转移方程
对第 i 个地块，有 2 种选择：
如果不放房子，则第 i-1 个地块可放可不放，即 dfs(i) = dfs(i-1)；
如果放房子，则第 i-1 个地块不能放房子，第 i-2 个地块可放可不放，即 dfs(i) = dfs(i-2)。
根据加法原理，两者相加即可，即 dfs(i) = dfs(i-1) + dfs(i-2)。
c.初始状态
dfs(0) = 1，表示不放是一种方案。
dfs(1) = 2，表示放和不放是两种方案。
d.答案
由于是两侧房屋放置方案数相互独立，根据乘法原理，为 dfs(n)**2。
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = dfs(i-1) + dfs(i-2) => dp[i] = dp[i-1] + dp[i-2]
dfs(0) = 1 => dp[0] = 1
dfs(1) = 2 => dp[1] = 2
dfs(n)**2 => dp[n]**2
"""

from functools import cache


class Solution2320:
    def countHousePlacements(self, n: int) -> int:
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     if i == 1:
        #         return 2
        #     return dfs(i - 1) + dfs(i - 2)
        #
        # MOD = 10**9 + 7
        # return (dfs(n) ** 2) % MOD

        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        return dp[n] ** 2 % MOD
