"""
思路：
由题意可知，本题必然使用二分查找解题。
虽然数组已按升序排列且无重复元素，但预先进行了旋转操作，不能直接用二分。
可以先比较 nums[i] 和 nums[-1] 的大小：
1.如果 nums[i] > nums[-1]，说明数组经过旋转后分为了左右两个递增段
2.如果 nums[i] <= nums[-1]，说明数组经过旋转后仍只有一个递增段
再比较 nums[mid] 和 target 的大小：
1.nums[mid] 和 target 在不同递增段上：
  a.nums[mid] 在第一段，target 在第二段，说明 target 在 nums[mid] 右侧
  b.nums[mid] 在第二段，target 在第一段，说明 target 在 nums[mid] 左侧
2.nums[mid] 和 target 在同一递增段上：
  a.nums[mid] > target，说明 target 在 nums[mid] 左侧
  b.nums[mid] < target，说明 target 在 nums[mid] 右侧
怎么将上述过程翻译成代码？
仅讨论 nums[mid] 在 target 右侧或者 nums[mid] 等于 target 的情况：
1.如果 nums[mid] > nums[-1]，说明 nums[mid] 在第一段上，
那么 target 也必须在第一段上且满足 nums[mid] >= target，才能说明 nums[mid] 和 target 都在第一段且 nums[mid] 在 target 右侧；
2.如果 nums[mid] < nums[-1]，说明 nums[mid] 在第二段上或者 nums 仅有一段，
那么 target 可以在第一段上，或者 target 在第二段上并满足 nums[mid] >= target，才能说明 nums[mid] 在 target 右侧。
"""

from typing import List


class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        def check(nums, i, target):
            if nums[i] > nums[-1]:
                return target > nums[-1] and nums[i] >= target
            else:
                return target > nums[-1] or nums[i] >= target

        n = len(nums)
        left, right = 0, n - 2
        while left <= right:
            mid = (left + right) // 2
            if check(nums, mid, target):
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] == target else -1
