"""
思路：
对每个数组元素 nums[i]，如果能知道 i 左侧的元素乘积和右侧的元素乘积即可求出 ans[i]，
使用前后缀的思想，定义 pre_prod[i] 表示 nums[0] 到 nums[i-1] 的乘积，suf_prod[i] 表示 nums[n-1] 到 nums[i+1] 的乘积
最终 ans[i] = pre_prod[i] * suf_prod[i]
"""

from typing import List


class Solution238:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf_prod = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_prod[i - 1] = suf_prod[i] * nums[i]
        pre_prod = 1
        for i, x in enumerate(nums):
            suf_prod[i] *= pre_prod
            pre_prod *= x
        return suf_prod[:-1]

        # n = len(nums)
        # pre_prod = [1] * (n + 1)
        # for i in range(n):
        #     pre_prod[i + 1] = pre_prod[i] * nums[i]
        # suf_prod = [1] * (n + 1)
        # for i in range(n - 1, -1, -1):
        #     suf_prod[i - 1] = suf_prod[i] * nums[i]
        # ans = []
        # for i in range(n):
        #     ans.append(pre_prod[i] * suf_prod[i])
        # return ans
