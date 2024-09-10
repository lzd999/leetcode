"""
思路：
本题与 LC740 类似，都是在某个区间上使用了打家劫舍的思想解题，
区别在于 LC740 关注的是元素出现次数，本题关注的是元素值。
因此在使用 Counter 维护出现次数后本题会对元素值进行排序。
1.记忆化搜索
a.状态定义
定义 dfs(i) 表示选择 nums[0...i] 后得到的伤害值之和的最大值。
b.状态转移方程
如果不选择 nums[i]，则 dfs(i) = dfs(i - 1)；
如果选择 nums[i]，表示 nums[i]-2、nums[i]-1、nums[i]+1、nums[i]+2 的元素值都能选，
那么能选的数 nums[j] 一定满足 nums[j] >= nums[i]-2，可以用二分，也可以用暴力查找 j 的索引。
两者取最大值即可。
c.初始状态
dfs(0) = 0，表示没有数可以选，伤害值为 0。
d.答案
dfs(n-1)
2.1:1翻译成递推
dfs(i) => dp[i]
dfs(i) = max(dfs(i - 1), dfs(j - 1) + x * cnt[x]) => dp[i] = max(dp[i-1], dp[j-1] + x * cnt[x])
dfs(0) = 0 => dp[0] = 0
dfs(n-1) => dp[-1]
"""

from collections import Counter
from functools import cache
from typing import List


class Solution3186:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     j = i
        #     x = nums[i]
        #     while j and nums[j - 1] >= x - 2:
        #         j -= 1
        #     return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
        #
        # cnt = Counter(power)
        # nums = sorted(cnt.keys())
        # n = len(nums)
        # return dfs(n - 1)

        cnt = Counter(power)
        nums = sorted(cnt.keys())
        n = len(nums)
        dp = [0] * (n + 1)
        for i, x in enumerate(nums):
            j = i
            while j and nums[j - 1] >= x - 2:
                j -= 1
            dp[i + 1] = max(dp[i], dp[j] + x * cnt[x])
        return dp[-1]
