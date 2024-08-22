"""
思路：
遍历每一行，如果 target 在某一行取值范围内，则对该行使用二分查找
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def lowerBound(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                idx = lowerBound(row, target)
                if idx != n and row[idx] == target:
                    return True
        return False
