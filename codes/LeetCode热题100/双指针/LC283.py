"""
思路：
定义双指针：p0 指向数组元素为 0 的位置，p 指向当前遍历到的位置
遍历数组，如果当前元素不为 0，则将当前元素 nums[p] 和 nums[p0] 交换位置，然后 p0 向后移动一位
"""

from typing import List


class Solution283:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = 0
        for p in range(n):
            if nums[p] != 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
