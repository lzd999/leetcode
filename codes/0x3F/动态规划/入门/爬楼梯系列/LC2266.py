"""
思路：
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示长度为 i 的字符串对应的文字信息种类数。
b.状态转移方程
如果 i 为 7 或 9，即可将连续的 4 个字符都视为一个字母，此时的状态转移方程为：
dfs(i) = dfs(i-1) + dfs(i-2) + dfs(i-3) + dfs(i-4)
如果 i 为 2、3、4、5、6、8，即可将连续的 3 个字符视为一个字母，此时的状态转移方程为：
dfs(i) = dfs(i-1) + dfs(i-2) + dfs(i-3)
c.初始状态
dfs(0) = 1，表示长度为 0 时的字符串为空串，对应的文字信息种类数为 1
d.答案
dfs(n)
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = dfs(i-1) + dfs(i-2) + dfs(i-3) + dfs(i-4) => dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
dfs(0) = 1 => dp[0] = 1
dfs(n) => dp[n]
"""

from functools import cache


class Solution2266:
    def countTexts(self, pressedKeys: str) -> int:
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     res = 0
        #     for j in range(1, MAPPING[pressedKeys[i - 1]] + 1):
        #         if i - j < 0 or pressedKeys[i - j] != pressedKeys[i - 1]:
        #             break
        #         res = (res + dfs(i - j)) % MOD
        #     return res
        #
        # MOD = 10**9 + 7
        # MAPPING = {
        #     "2": 3,
        #     "3": 3,
        #     "4": 3,
        #     "5": 3,
        #     "6": 3,
        #     "7": 4,
        #     "8": 3,
        #     "9": 4,
        # }
        # n = len(pressedKeys)
        # return dfs(n)

        MOD = 10**9 + 7
        MAPPING = {
            "2": 3,
            "3": 3,
            "4": 3,
            "5": 3,
            "6": 3,
            "7": 4,
            "8": 3,
            "9": 4,
        }
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, MAPPING[pressedKeys[i - 1]] + 1):
                if i - j < 0 or pressedKeys[i - j] != pressedKeys[i - 1]:
                    break
                dp[i] = (dp[i] + dp[i - j]) % MOD
        return dp[-1]
