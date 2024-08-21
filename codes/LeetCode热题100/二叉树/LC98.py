"""
思路：
二叉搜索树的一个重要性质：对任意节点来说，左子树值 < 当前节点值 < 右子树值，
1.递归
a.边界条件：当前节点为空，
b.递归条件：判断当前节点值是否满足性质，再递归判断左右子树是否满足性质。 
2.迭代
如果对二叉搜索树进行中序遍历，根据其性质可以得到一个严格递增序列，每次迭代到下一个节点前，将当前节点赋给前驱节点 pre
"""

from typing import Optional
from math import inf
from leetcode.utils.tree_node import TreeNode


class Solution98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if node is None:
                return True
            return left < node.val < right and dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, -inf, inf)

        # st = [(root, False)]
        # pre = None
        # while st:
        #     node, visited = st.pop()
        #     if node is None:
        #         continue
        #     if not visited:
        #         st.append((node.right, False))
        #         st.append((node, True))
        #         st.append((node.left, False))
        #     else:
        #         if pre is not None and pre.val >= node.val:
        #             return False
        #         pre = node
        # return True
