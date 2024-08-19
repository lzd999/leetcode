"""
思路：
※ 本题虽然出现了“子数组”，看似可以用滑动窗口，但滑动窗口需要满足单调性，即当下一个元素进入滑动窗口时，
   滑动窗口内的元素和不能减少，但题目数据范围说明了数组元素可能为负数，可能会导致滑动窗口的元素和减少，需要移动左边界
求子数组连续元素和的一个方法是使用前缀和：
即定义 pre_sum 数组，长度为 n+1，且满足 pre_sum[i+1] = pre_sum[i] + nums[i]
第一次遍历 nums，计算 pre_sum 数组；
第二次遍历 pre_sum，使用哈希表维护 i 满足 i < j 且 pre_sum[i] = pre_sum[j] - k 的个数，
没有则加 1，有则累加当前哈希表维护的个数
"""

from collections import defaultdict
from typing import List


class Solution560:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # pre_sum = [0] * (n + 1)
        # for i in range(n):
        #     pre_sum[i + 1] = pre_sum[i] + nums[i]
        # cnt = defaultdict(int)
        # ans = 0
        # for s in pre_sum:
        #     if s - k in cnt:
        #         ans += cnt[s - k]
        #     cnt[s] += 1
        # return ans

        ans = 0
        pre_sum = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # 避免特判 pre_sum[0] = 0 的情况
        for x in nums:
            pre_sum += x
            # ans 和 cnt 的更新能否交换顺序？
            # 不能。举个例子，nums = [2]，k = 0，正确结果是 0
            # 如果先更新 cnt 再更新 ans，会出现答案为 1 的错误情况
            if pre_sum - k in cnt:
                ans += cnt[pre_sum - k]
            cnt[pre_sum] += 1
        return ans
