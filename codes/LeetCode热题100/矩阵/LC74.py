"""
思路：
参考 LC240.搜索二维矩阵 II
"""

from bisect import bisect_left
from typing import List


class Solution74:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[-1]:
                idx = bisect_left(row, target)
                if idx == n or row[idx] != target:
                    return False
                else:
                    return True
        return False
