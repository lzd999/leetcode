"""
思路：
观察示例 1 可以清楚输出不在意顺序，因此可先对当前数组排序，再使用双指针
需要注意的是：
如果存在重复数字，则需要跳过重复数字；
如果存在连续三个数加和大于 0，则需要跳出循环，因为在对数组排序后，后续不可能出现连续三个数加和为 0
如果当前数字和最后两个数加和都小于 0，则需要继续循环，因为在对数组排序后，后续可能出现某个数使得这三个数的加和为 0
"""

from typing import List


class Solution15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    k -= 1
                    while k > j and nums[k + 1] == nums[k]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return ans
