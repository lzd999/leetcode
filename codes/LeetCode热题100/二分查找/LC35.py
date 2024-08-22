"""
思路：
在有序数组查找目标元素，且时间复杂度为 O(logN)，必然要使用二分查找。
二分查找的过程如下：
定义 left 和 right 为查找区间的左右边界，每次比较查找区间的中间位置 mid 对应元素与 target 的大小：
1.如果 mid 对应元素等于 target，则返回 mid；
2.如果 mid 对应元素小于 target，则说明 target 在 mid 的右侧，令 left = mid + 1；
3.如果 mid 对应元素大于 target，则说明 target 在 mid 的左侧，令 right = mid - 1。
重复上述过程，直到 left > right，此时查找区间为空，返回 left 即可。
"""

from typing import List


class Solution35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
