"""
思路：
如果不删除当前位置 i 的数，则当前结果为删除位置为 i-1 的数的最优结果；
如果删除当前位置 i 的数，则当前结果为删除位置为 i-2 的数的最优结果 + 当前位置 i 的数 * 出现频次；
这两种结果取最大值，即为当前位置 i 的最优结果。
可以发现，这和打家劫舍问题非常相似。
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示处理前 i 个数字所能获得的最大点数。
b.状态转移方程
对数字 i，有两种情况：
如果不删除数字 i，则最大点数为删除数字 i-1 能获得的最大点数，即 dfs(i) = dfs(i-1)；
如果删除数字 i，则最大点数为删除数字 i-2 能获得的最大点数 + i * 出现频次，即 dfs(i) = dfs(i-2) + i * cnt[i]；
两种情况取最大值即可，即 dfs(i) = max(dfs(i-1), dfs(i-2) + i * cnt[i])。
c.初始状态
dfs(0) = 0，表示初始点数为 0。
dfs(1) = cnt[1]，表示截止到数字 1，所能获得的最大点数为 1 * cnt[1] = cnt[1]。
d.答案
dfs(max(nums))，表示截止最大数字，所能获得的最大点数。
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = max(dfs(i-1), dfs(i-2) + i*cnt[i]) => dp[i] = max(dp[i-1], dp[i-2] + i*cnt[i)
dfs(0) = 0 => dp[0] = 0
dfs(1) = cnt[1] => dp[1] = cnt[1]
dfs(max(nums)) => dp[max(nums)]
"""

from collections import Counter
from functools import cache
from typing import List


class Solution740:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if i == 1:
        #         return cnt[1]
        #     return max(dfs(i - 1), dfs(i - 2) + i * cnt.get(i, 0))
        #
        # cnt = Counter(nums)
        # return dfs(max(nums))

        # cnt = Counter(nums)
        # dp = [0] * (max(nums) + 1)
        # dp[1] = cnt[1]  # nums = [1]
        # for i in range(2, max(nums) + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + i * cnt[i])
        # return dp[max(nums)]

        cnt = Counter(nums)
        f0, f1 = 0, cnt[1]
        for i in range(2, max(nums) + 1):
            new_f = max(f1, f0 + i * cnt[i])
            f0 = f1
            f1 = new_f
        return f1
