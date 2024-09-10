"""
思路：
由题意可知，本题的实质就是 LC70.爬楼梯：
每次从 nums 中选一个数作为向上爬的台阶数，爬 target 阶的方案数。
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示爬 i 个台阶的方案数。
b.状态转移方程
爬到第 target 阶时选择了爬 nums[j] 阶，那么方案数即为 dfs(i - nums[j])。
即 dfs(i) = Σdfs(i - nums[j]) j ∈ [0, n-1]
c.初始状态
dfs(0) = 1，表示 target 台阶正好爬完。
d.答案
dfs(target)
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = Σdfs(i - nums[j]) j ∈ [0, n-1] => dp[i] = Σdp[i - nums[j]] j ∈ [0, n-1]
dfs(0) = 1 => dp[0] = 1 
dfs(target) => dp[-1]
"""

from functools import cache
from typing import List


class Solution377:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return 1
            res = 0
            for x in nums:
                if x <= i:
                    res += dfs(i - x)
            return res

        return dfs(target)

        # dp = [1] + [0] * target
        # for i in range(1, target + 1):
        #     for x in nums:
        #         if x <= i:
        #             dp[i] += dp[i - x]
        # return dp[-1]
