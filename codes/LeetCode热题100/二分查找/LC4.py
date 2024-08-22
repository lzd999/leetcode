"""
思路：
由题意可知是使用二分查找求两个升序数组合并后的中位数。
为了避免因为合并后数组长度的奇偶性影响，可以在数组间隙加上虚拟符号，取索引时除 2 下取整即可。
加入虚拟符号后，nums1 的长度由 m 变为了 2m+1，nums2 的长度由 n 变为了 2n+1，总长度即为 2m+2n+2，恒为偶数。
现在合并后数组的中位数必然是对靠近中间的左右两数进行加和除以 2，现在本题的关键在于如何找这两个数。
设 ci 为第 i 个数组的分割线，left_maxi 为第 i 个数组切分后左半部分的最大元素，right_mini 为第 i 个数组切分后右半部分的最小元素。
对本题，c1、c2 为两个数组的分割线，left_max1、left_max2 为两个数组切分后左半部分的最大元素，right_mini1、right_mini2 为两个数组切分后右半部分的最小元素。
切分后可能存在以下情况：
1.left_max1 > right_min2，说明第 1 个数组左半部分的元素太多，需要左移分割线 c1；
2.left_max2 > right_mini1，说明第 2 个数组左半部分的元素太多，需要左移分割线 c2；
3.某个数组的所有元素完全小于中位数：
  a.c1 = 2*n，说明 nums1 元素都比中位数小，切分后 nums1 右半部分为空，可以令 right_min1 为正无穷；
  b.c2 = 2*n，说明 nums2 元素都比中位数小，切分后 nums2 右半部分为空，可以令 right_min2 为正无穷；
4.某个数组的所有元素完全大于中位数：
  a.c1 = 0，说明 nums1 元素都比中位数大，切分后 nums1 左半部分为空，可以令 left_max1 为负无穷；
  b.c2 = 0，说明 nums2 元素都比中位数大，切分后 nums2 左半部分为空，可以令 left_max2 为负无穷。
"""

from math import inf
from typing import List


class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, 2 * m  # 初始化右边界为 2m 是为了提高二分查找的效率
        while left <= right:
            c1 = (left + right) // 2
            c2 = (m + n) - c1

            left_max1 = -inf if c1 == 0 else nums1[(c1 - 1) // 2]
            right_min1 = inf if c1 == 2 * m else nums1[c1 // 2]
            left_max2 = -inf if c2 == 0 else nums2[(c2 - 1) // 2]
            right_min2 = inf if c2 == 2 * n else nums2[c2 // 2]

            if left_max1 > right_min2:
                right = c1 - 1
            elif left_max2 > right_min1:
                left = c1 + 1
            else:
                break

        return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
