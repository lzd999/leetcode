"""
思路：
暴力做法是遍历数组，对每个元素 x，以 x 为起点，判断 x+1,x+2,……是否都在 nums 中
假设找到的最大连续元素为 x+k，可以得到以 x 为起点的最长连续序列长度为 k+1。
怎么优化？
a.判断 x+1,x+2,……是否在 nums 存在这一步可以用哈希表优化 
b.如果当前数组本身就是连续元素构成，例如 nums = [1,2,3,4,5]，每次判断会产生冗余工作：
  第一次对元素 1，以 1 为起点判断了 2,3,4,5 发现都在 nums 数组中；
  第二次对元素 2，以 2 为起点判断了 3,4,5 发现都在 nums 数组中。
  不仅出现了重复判断，且无法更新最长连续序列长度。
  可以考虑用哈希表先判断 x-1 是否存在于 nums 中，如果存在则直接跳过，
  不存在则说明 x 可能为最长连续序列的起点，再判断 x+1,x+2,……是否都在 nums 中。
"""

from typing import List


class Solution128:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 哈希表
        nums_set = set(nums)
        ans = 0
        for x in nums_set:
            cur = x
            if (cur - 1) not in nums_set:
                while (cur + 1) in nums_set:
                    cur += 1
            ans = max(ans, cur - x + 1)
        return ans
