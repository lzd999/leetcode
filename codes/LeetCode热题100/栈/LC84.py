"""
思路：
观察示例 1，最直观的做法是枚举以每个柱子为高度的最大矩形的面积，从中找出最大值。
可以发现，这种做法需要找到左右两边下一个更小元素，因此可以使用单调栈。
假设 h = heights[i] 是矩形的高度，我们怎么使用单调栈知道矩形的最大宽度？
在 i 左侧的小于 h 的最近元素的索引 left，如果不存在则为 −1。求出了 left，那么 left + 1 就是在 i 左侧的大于等于 h 的最近元素的索引。
在 i 右侧的小于 h 的最近元素的索引 right，如果不存在则为 n。求出了 right，那么 right − 1 就是在 i 右侧的大于等于 h 的最近元素的索引。
"""

from typing import List


class Solution84:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        st = []
        for i, x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st.clear()
        right = [n] * n
        for i in range(n - 1, -1, -1):
            x = heights[i]
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans
