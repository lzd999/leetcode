"""
思路：
本题与 LC198.打家劫舍 的区别是房屋围成了一圈，即数组 nums 变为了环形数组，
在 LC198.打家劫舍 的基础上，还要考虑 nums[0] 是否会被偷：
1.如果偷 nums[0]，则剩余可偷的房屋为 nums[2] 到 nums[-2]；
2.如果不偷 nums[0]，则剩余可偷的房屋为 nums[1] 到 nums[-1]；
两种情况取最大值即可。
"""

from typing import List


class Solution213:
    def rob198(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            new_f = max(f1, f0 + x)
            f0 = f1
            f1 = new_f
        return f1

    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.rob198(nums[2:-1]), self.rob198(nums[1:]))
