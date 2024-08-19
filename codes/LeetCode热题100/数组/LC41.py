"""
思路：
一般做法是：
1.定义哈希表维护每个数组元素是否出现，然后遍历哈希表，如果未出现则返回该元素，否则返回数组长度+1
2.对数组排序，使用二分找到找到第一个未出现的元素
但题目要求了时间复杂度为 O(n)，空间复杂度为 O(1)，这意味着不能额外创建哈希表或者不能对数组排序
这种情况下可以考虑“原地哈希”，即将原数组当做哈希表使用
具体步骤如下：
假设未出现的数为 x，则 x ∈ [1,n]，最后如果都找到了，则返回 n+1，
遍历当前数组，将 1 放在 nums[0] 位置，将 2 放在 nums[1] 位置......按照这种思路重新整理数组，
再遍历一遍数组，返回第一个 nums[i] ≠ i+1 的位置，
可以看出，所谓的“原地哈希”，本质上相当于自定义哈希函数。本题自定义的哈希函数为 hash(nums[i]) = nums[i] - 1
"""

from typing import List


class Solution41:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

        # def lowerBound(nums, target):
        #     left, right = 0, n - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             return mid
        #         if nums[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return -1
        #
        # n = len(nums)
        # nums.sort()
        # for i in range(1, n + 1):
        #     if lowerBound(nums, i) == -1:
        #         return i
        # return n + 1

        # n = len(nums)
        # nums_set = set(nums)
        # for i in range(1, n + 1):
        #     if i not in nums_set:
        #         return i
        # return n + 1

