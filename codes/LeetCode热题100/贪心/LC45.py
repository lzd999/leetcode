"""
思路：
本题的思路与 LC55.跳跃游戏 相似，使用贪心解题。
定义 cur_loc 维护当前位置，max_loc 维护从当前位置能跳跃到的最远位置。
遍历数组，每次更新从当前位置能跳跃到的最远位置 max_loc，
如果 cur_loc 与 i 相等，说明最远位置达到上限了，更新当前位置为最远到达位置，并增加跳跃次数。
"""

from typing import List


class Solution45:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cur_loc = max_loc = 0
        for i in range(n - 1):
            max_loc = max(max_loc, i + nums[i])
            if i == cur_loc:
                cur_loc = max_loc
                ans += 1
        return ans
