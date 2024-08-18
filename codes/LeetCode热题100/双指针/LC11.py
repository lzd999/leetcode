"""
思路：
由题意可知，容器储存的水的容量取决于可容纳水的高度和两个容器间的宽度，
可以考虑使用双指针使得两个容器间的宽度最大，即定义 left 和 right 初始化为 0 和 n-1 指向首尾元素，
然后比较 left 和 right 对应的高度 height[left] 和 height[right]，取较小值，
此时容器储存水的容量为 (right - left) * min(height[left], height[right])，
更新最大储水量并向中间移动对应指针
"""

from typing import List


class Solution11:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
