"""
思路：
岛屿类问题是网格图问题使用 DFS 解决的典型问题。
岛屿类问题会将网格图的 1 视作陆地，0 视作海洋，
DFS 解决岛屿类问题的一般做法：
遍历网格图的每个网格，再以该网格为起点遍历其上下左右四个方向，如果某个方向临时超出边界或者已经被遍历过，则直接返回。
回到本题，每次遇到陆地后对其使用 DFS，并对四个方向继续进行 DFS，直至遇到海洋或者超出边界，
说明当前的陆地已全部遍历，答案加 1。
"""

from typing import List


class Solution200:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":
                return
            if grid[r][c] == "-1":
                return
            grid[r][c] = "-1"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        m, n = len(grid), len(grid[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1
        return ans
