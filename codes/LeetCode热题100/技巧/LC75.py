"""
思路：
本题是经典的【荷兰国旗问题】。
根据题目的描述，我们需要将数组中的 0，1，2 分别放到数组的左边，中间，右边这三段。
定义 i 表示当前遍历的元素 nums[i] 的索引，p0 表示需要填 0 的索引，p2 表示需要填 2 的索引。
遍历当前数组，遇到 0 则交换 i 和 p0，同时 p0 向右移动；遇到 1 则 i++；遇到 2 则交换 i 和 p2，同时 p2 向左移动。
"""

from typing import List


class Solution75:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:  # 为什么不用 for？
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
