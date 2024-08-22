"""
思路：
“返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数”，这句话的实质是求腐烂橘子到所有新鲜橘子的最短路径！！！
在网格图问题中，使用 BFS 可以求每个节点到其他节点的最短路径，这与本题的实质是一样的。
对网格图进行两次遍历：
a.第一次遍历，统计新鲜橘子的数量 fresh ，用队列 q 存储腐烂橘子的坐标
b.第二次遍历，对每个腐烂橘子的相邻节点使用 BFS，如果相邻节点存在新鲜橘子，则新鲜橘子数量减 1，并将当前橘子的坐标入队
  初始腐烂橘子的坐标遍历完后，经过的分钟数加 1，直至队列为空或者新鲜橘子数量为 0。
c.如果存在新鲜橘子，返回 -1，否则返回经过的时间
"""

from collections import deque
from typing import List


class Solution994:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((r, c))
        ans = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for r, c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))
            ans += 1
        return -1 if fresh > 0 else ans
