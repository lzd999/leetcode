"""
思路：
定义 L 和 R 指向查找区间的左右边界，即闭区间 [L,R]；
定义 M 指向查找区间里准备与 target 比较的数的索引；
定义 Red 表示 False，表示 < target 的数；Blue 表示 True，表示 >= target 的数；White 表示不确定的数；
最开始 L 和 R 指向整个数组的左右边界，即 L = 0，R = n - 1；
如果令 M = (L + R) // 2，我们可以立刻得知当前区间一半元素与 target 的关系：
a.nums[M] < target，说明 [L,M] 都是 Red，剩余不确定区间为 [M+1,R]，下一步应该令 L = M + 1，同时说明 L - 1 指向的一定是 Red；
b.nums[M] > target，说明 [M,R] 都是 Blue，剩余不确定区间为 [L,M-1]，下一步应该令 R = M - 1，同时说明 R + 1 指向的一定是 Blue；
不断重复上述步骤，直到 L > R。
可以发现，查找过程的关键在于循环不变量，即 L - 1 指向的一定是 Red，R + 1 指向的一定是 Blue，
最终 R + 1 指向的即是当前区间里第一个 >= target 的数的索引，根据循环不变量，返回 L。
可以发现，整个过程的本质就是对查找区间进行二分查找，返回有序数组第一个 >= target 的数的索引，如果不存在，则返回数组长度。
那如果是 >、<、≤ 呢？
> target：>= (target + 1)
< target：(>= target) - 1
≤ target：(> target) - 1 => (>= target + 1) - 1

回到本题，我们首先使用上述方法找到第一个 >= target 的数的索引 start，即 target 的第一个位置；
如果 start 等于数组长度或者 nums[start] 不等于 target，则返回 [-1,-1]；
再使用上述方法找到第一个 > target 的数的索引 end；
最后返回 [start,end] 即可。
"""

from typing import List


class Solution34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        n = len(nums)
        start = lowerBound(nums, target)
        if start == n or nums[start] != target:
            return [-1, -1]
        end = lowerBound(nums, target + 1) - 1
        return [start, end]
