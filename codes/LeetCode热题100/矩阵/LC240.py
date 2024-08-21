"""
思路：
1.二分查找
由题意可知，矩阵每一行具备单调性，因此可使用二分查找
遍历矩阵每一行，如果 target 大于当前行最后一个元素或者小于第一个元素，则直接跳过；
否则对当前行使用二分查找，如果索引不越界且对应值为 target，则返回 True，否则返回 False
2.分治
如果将矩阵逆时针旋转45°，可以发现其结构类似二叉搜索树：相邻的左节点小于当前值，相邻的右节点大于当前值。
那么可以考虑从右上角元素开始：
如果当前元素小于 target，说明当前行元素都小于 target，排除当前行；
如果当前元素大于 target，说明当前列元素都大于 target，排除当前列；
如果当前元素等于 target，则返回 True；
否则返回 False
"""

from bisect import bisect_left
from typing import List


class Solution240:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # for row in matrix:
        #     if target < row[0] or target > row[-1]:
        #         continue
        #     if row[0] <= target <= row[-1]:
        #         idx = bisect_left(row, target)
        #         if idx != n and row[idx] == target:
        #             return True
        # return False

        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
