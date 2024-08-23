"""
思路：
观察示例 1，nums = [2,3,1,1,4]
位于索引 0，能到达的最远索引为 0+2=2，即跳跃区间为 [0,2]；
位于索引 1，能到达的最远索引为 1+3=4，即跳跃区间为 [1,4]；
位于索引 2，能到达的最远索引为 2+1=5，即跳跃区间为 [2,3]；
位于索引 3，能到达的最远索引为 3+1=4，即跳跃区间为 [3,4]；
位于索引 4，能到达的最远索引为 4+4=4，即跳跃区间为 [4,8]；
如果合并跳跃区间可以发现最终能合并为一个大区间 [0,8]，返回为 True。
再观察示例 2，nums = [3,2,1,0,4]
位于索引 0，能到达的最远索引为 0+3=3，即跳跃区间为 [0,3]；
位于索引 1，能到达的最远索引为 1+2=3，即跳跃区间为 [1,3]；
位于索引 2，能到达的最远索引为 2+1=3，即跳跃区间为 [2,3]；
位于索引 3，能到达的最远索引为 3+0=3，即跳跃区间为 [3,3]；
位于索引 4，能到达的最远索引为 4+4=8，即跳跃区间为 [4,8]；
如果合并跳跃区间可以发现最终合并得到两个大区间，即 [0,3] 和 [4,8]，返回为 False。
可以得出结论：合并每个跳跃区间 [i,i+nums[i]]，如果能合成一个大区间，返回为 True，否则返回为 False。
因此本题可以用 LC.56 合并区间 的思想理解。
定义 max_loc 表示从当前下标能跳跃的最远位置，
根据上述分析过程，遍历 nums，如果当前下标比 max_loc 大，即无法从上一个下标跳跃到当前下标，直接返回 False，
更新 max_loc，如果已经跳跃到了 nums 的最后一个位置，可提前返回 True。
"""

from typing import List


class Solution55:
    def canJump(self, nums: List[int]) -> bool:
        max_loc = 0
        for i, x in enumerate(nums):
            if i > max_loc:
                return False
            max_loc = max(max_loc, i + x)
            if max_loc >= len(nums) - 1:
                return True

        # max_loc = 0
        # for i, x in enumerate(nums):
        #     if i > max_loc:
        #         return False
        #     max_loc = max(max_loc, i + x)
        # return True
