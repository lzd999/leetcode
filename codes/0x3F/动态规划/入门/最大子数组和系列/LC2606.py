"""
思路：
将 s 的每个字符按照题目的规则映射到相应的数字上，这些数字组成数组 nums，就转化成了 LC53.最大子数组和。
定义 mapping 保存 chars 数组和 vals 数组的映射。
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示以 nums[i] 结尾的最大子数组和。
b.状态转移方程
先通过 mapping 找到当前字符 s[i] 对应的 nums[i]，再计算 dfs(i) = max(dfs(i - 1), 0) + nums[i]。
c.初始状态
dfs(0) = 0，表示当前位置之前没有字符，所以以当前字符结尾的最大子数组和为 0。
d.答案
max(dfs(i))
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = max(dfs(i-1), 0) + nums[i] => dp[i] = max(dp[i-1], 0) + nums[i]，nums[i] = mapping.get(s[i], ord(s[i]) - ord("a") + 1)
dfs(0) = 0 => dp[0] = 0
max(dfs(i)) => max(dp[i])
"""

from functools import cache
from typing import List


class Solution2606:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i - 1), 0) + mapping.get(s[i], ord(s[i]) - ord("a") + 1)
        #
        # n = len(s)
        # mapping = dict(zip(chars, vals))
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, dfs(i))
        # return ans

        # n = len(s)
        # ans = 0
        # mapping = dict(zip(chars, vals))
        # dp = [0] * n
        # for i, cs in enumerate(s):
        #     dp[i] = max(dp[i - 1], 0) + mapping.get(cs, ord(cs) - ord("a") + 1)
        #     ans = max(ans, dp[i])
        # return ans

        ans = 0
        mapping = dict(zip(chars, vals))
        dp = 0
        for cs in s:
            dp = max(dp, 0) + mapping.get(cs, ord(cs) - ord("a") + 1)
            ans = max(ans, dp)
        return ans
