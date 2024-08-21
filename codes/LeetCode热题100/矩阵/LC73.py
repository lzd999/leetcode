"""
思路：
O(mn) 的额外空间是重新创建一个矩阵，O(m+n) 的额外空间是定义标记数组表示当前矩阵格是否为 0
仅使用 O(1) 的额外空间必然是原地修改矩阵，但可能会丢失原本的矩阵元素是否为 0
可以将矩阵的第一行和第一列作为标记变量 row_0 和 col_0，
前两次遍历分别判断第一行和第一列是否存在 0，
第三次遍历矩阵除第一行和第一列外的其他元素，如果某个矩阵元素为 0，则将当前行和当前列对应的第一行和第一列元素置 0
第四次遍历矩阵，如果当前矩阵元素对应的第一行和第一列元素为 0，则将当前矩阵元素置 0，
最后根据第一行和第一列的标记变量判断是否将第一行和第一列的所有元素置 0
"""

from typing import List


class Solution73:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_0 = col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_0 = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                col_0 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_0:
            for i in range(m):
                matrix[i][0] = 0
        if col_0:
            for j in range(n):
                matrix[0][j] = 0
