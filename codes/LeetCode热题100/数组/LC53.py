"""
思路：
“子数组”“最大和”+数组元素可能为负数，综合考虑可以使用前缀和将连续子数组的和转化为某两个前缀和的差，
与 LC121.买卖股票的最佳时机 类似，第一次遍历数组求解前缀和，第二次遍历前缀和求解最小前缀和和最大前缀和之差。
"""

from math import inf
from typing import List


class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        pre_sum = min_pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans
