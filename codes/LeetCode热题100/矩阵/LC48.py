"""
思路：
由于题意要求原地旋转矩阵，因此无法使用辅助矩阵
观察示例 1 可以发现 matrix[i][j] -> matrix[j][n-1-i] 行列互换且交换行列
可以考虑将旋转操作转化成对称操作
矩阵的对称操作有如下四种：
a.上下对称：matrix[i][j] -> matrix[n-1-i][j]，可以发现列不变
b.左右对称：matrix[i][j] -> matrix[i][n-1-j]，可以发现行不变
c.主对角线对称：matrix[i][j] -> matrix[j][i]，可以发现行列互换
d.副对角线对称：matrix[i][j] -> matrix[n-1-j][n-1-i] ，可以发现行列均变，且互换
根据四种对称操作对应的转换式，可以发现可以先进行主对角线对称，再进行左右对称即可
"""

from typing import List


class Solution48:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def up_down_symmetry(matrix):
            """
            上下对称
            """
            for i in range(n // 2):
                for j in range(n):
                    matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        def left_right_symmetry(matrix):
            """
            左右对称
            """
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

        def main_diagonal_symmetry(matrix):
            """
            主对角线对称
            """
            for i in range(n - 1):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def sub_diagonal_symmetry(matrix):
            """
            副对角线对称
            """
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]

        main_diagonal_symmetry(matrix)
        left_right_symmetry(matrix)
