"""
思路：
由题意可知，可将全部课程抽象为一个有向图，每节课抽象为图的一个节点，每门课程的先修课程抽象为图的一个有向边，
该有向边由 bi 指向 ai，表示必须先选修课程 bi 才能选修课程 ai。
至此，整个题被抽象成了一个有向图，最终求解的实质是判断该有向图是否为有向无环图 DAG。
如何判断有向图是否为 DAG？拓扑排序。
a.根据题意先抽象为有向图
b.先统计每个节点的入度 in_degrees
c.用队列统计所有入度为 0 的节点
d.遍历队列，将节点出队，遍历该节点的邻接节点，将邻接节点的入度减一，如果入度为 0，则将节点入队
e.重复 d 直至队列为空，最后判断所有节点的入度是否均为 0，是则返回 True，否则返回 False
"""

from collections import deque
from typing import List


class Solution207:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        edges = prerequisites

        # BFS
        in_degrees = [0] * n
        g = [[] for _ in range(n)]
        for x, y in edges:
            in_degrees[x] += 1
            g[y].append(x)
        q = deque()
        for i in range(n):
            if not in_degrees[i]:
                q.append(i)
        while q:
            node = q.popleft()
            n -= 1
            for x in g[node]:
                in_degrees[x] -= 1
                if not in_degrees[x]:
                    q.append(x)
        return n == 0

        # DFS
        # def dfs(i, g, visited):
        #     if visited[i] == -1:
        #         return True
        #     if visited[i] == 1:
        #         return False
        #     visited[i] = 1
        #     for j in g[i]:
        #         if not dfs(j, g, visited):
        #             return False
        #     visited[i] = -1
        #     return True
        #
        # g = [[] for _ in range(n)]
        # visited = [0] * n
        # for x, y in edges:
        #     g[y].append(x)
        # for i in range(n):
        #     if not dfs(i, g, visited):
        #         return False
        # return True
