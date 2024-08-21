"""
思路：
按照题意模拟即可：
1.定义矩阵的上下左右边界：up、down、left、right
2.先向右移动至右边界，结束后上边界向下移动，如果上边界大于下边界，则说明矩阵无法遍历，终止循环；
3.再向下移动至下边界，结束后右边界向左移动，如果右边界小于左边界，则说明矩阵无法遍历，终止循环；
4.接着向左移动至左边界，结束后下边界向上移动，如果下边界小于上边界，则说明矩阵无法遍历，终止循环；
5.最后向上移动至上边界，结束后左边界向右移动，如果左边界大于右边界，则说明矩阵无法遍历，终止循环；
"""

from typing import List


class Solution54:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        up, down = 0, m - 1
        left, right = 0, n - 1
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans
