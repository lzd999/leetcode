"""
思路：
由题意可知，本题的实质就是 LC70.爬楼梯：
每次可以爬 zero 或 one 个台阶，返回爬到 low 到 high 个台阶的方案数。
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示构造长度为 i 的字符串的方案数。
b.状态转移方程
(1) 在长度为 i 的字符串末尾插入 zero 个 '0'，即 dfs(i) = dfs(i-zero)。
(2) 在长度为 i 的字符串末尾插入 one 个 '1'，即 dfs(i) = dfs(i-one)。
根据加法原理，dfs(i) = dfs(i-zero) + dfs(i-one)，注意取余。
c.初始状态
dfs(0) = 1，表示构造空串的方案数为 1。
d.答案
Σ dfs(i) i ∈ [low, high]
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = dfs(i-zero) + dfs(i-one) => dp[i] = dp[i-zero] + dp[i-one]
dfs(0) = 1 => dp[0] = 1
Σ dfs(i) i ∈ [low, high] => Σ dp[i] i ∈ [low, high]
"""

from functools import cache


class Solution2466:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     return (dfs(i - zero) + dfs(i - one)) % MOD
        #
        # MOD = 1_000_000_007
        # ans = 0
        # for i in range(low, high + 1):
        #     ans = (ans + dfs(i)) % MOD
        # return ans

        MOD = 1_000_000_007
        dp = [1] + [0] * high
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % MOD
        return ans
