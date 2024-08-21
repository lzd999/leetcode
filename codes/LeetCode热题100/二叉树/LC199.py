"""
思路：
二叉树的每一层都存在最右侧节点，最直接的做法就是对二叉树进行层序遍历（bfs），
需要注意的是入队顺序为先右后左，而且要记录当前的节点是第几个，如果是第 1 个节点，则直接加入答案。
"""

from collections import deque
from typing import Optional, List
from leetcode.utils.tree_node import TreeNode


class Solution199:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                if i == 0:
                    ans.append(node.val)
        return ans

        # def dfs(node, depth):
        #     if node is None:
        #         return
        #     if len(ans) == depth:  # 当前的节点数等于深度数，表示是新的一层的第一个节点
        #         ans.append(node.val)  # 加入答案
        #     dfs(node.right, depth + 1)  # 入栈顺序为先右后左
        #     dfs(node.left, depth + 1)
        #
        # ans = []
        # dfs(root, 0)
        # return ans
