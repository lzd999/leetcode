"""
思路：
核心是比较 nums[mid] 和 nums[-1] 的大小：
如果 nums[mid] > nums[-1]，说明 nums 被旋转成了两个递增序列且 nums[mid] 在第一段递增序列，nums[mid] 一定在最小值左边
如果 nums[mid] ≤ nums[-1]，说明最小值要么是 nums[mid]，要么在 nums[mid] 左边
"""

from typing import List


class Solution153:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]