"""
思路：
怎么理解杨辉三角？
杨辉三角的实质是组合数的恒等式，即 C[i][j] = C[i-1][j-1] + C[i-1][j]，C[0][0] = 1。
很明显，这是一个递推式，可以转化为动态规划。
1.状态定义
定义 C[i][j] 表示从 i 个不同物品中选出 j 个物品的方案数。
2.状态转移方程
站在第 i 个物品选或不选的角度，
如果选第 i 个物品，即从 i-1 个不同物品中选出 j-1 个物品的方案数，即 C[i-1][j-1]；
如果不选第 i 个物品，即从 i-1 个不同物品中选出 j 个物品的方案数，即 C[i-1][j]；
根据加法原理，C[i][j] = C[i-1][j-1] + C[i-1][j]。
3.状态初始化
C[0][0] = 1，表示从 0 个不同物品中选出 0 个物品的方案数，即 1。
4.目标函数
返回 C[numRows-1][0] 到 C[numRows-1][numRows-1] 的所有方案数。
"""

from typing import List


class Solution118:
    def generate(self, numRows: int) -> List[List[int]]:
        C = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
        return C
