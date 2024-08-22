"""
思路：
模拟维基百科上对下一个排列的定义的生成过程即可。
1.先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
2.再找出另一个最大索引 l 满足 nums[l] > nums[k]；
3.交换 nums[l] 和 nums[k]；
4.最后翻转 nums[k+1:]。
"""

from typing import List


class Solution31:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        idx1 = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx1 = i
                break
        if idx1 == -1:
            reverse(nums, 0, n - 1)
            return
        idx2 = -1
        for i in range(n - 1, idx1, -1):
            if nums[i] > nums[idx1]:
                idx2 = i
                break
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        reverse(nums, idx1 + 1, n - 1)
