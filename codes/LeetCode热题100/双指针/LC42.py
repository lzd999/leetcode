"""
思路：
本题可看做是 LC11.盛最多水的容器 的进阶题，区别在于 LC11 求的是最大，本题求的是加和。
使用双指针：定义 left 和 right 分别指向最左和最右的柱子，然后向中间移动；
定义 pre_max 和 suf_max 记录左侧和右侧最大高度，初始化为 0；
每次比较当前左侧最大高度 pre_max 和 height[left]，取较大值并更新 pre_max，
同理比较当前右侧最大高度 suf_max 和 height[right]，取较大值并更新 suf_max；
如果 pre_max < suf_max，说明左侧还有空间接水，向右移动左指针，同时累加接水量为 pre_max - height[left]；
如果 suf_max < pre_max，说明右侧还有空间接水，向左移动右指针，同时累加接水量为 suf_max - height[right]。
"""

from typing import List


class Solution42:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        pre_max = suf_max = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
