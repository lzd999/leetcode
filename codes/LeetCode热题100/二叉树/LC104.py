"""
思路：
1.递归：
a.终止条件：如果当前节点为空，返回 0
b.递归过程：使用递归函数获取左右子树的最大深度，当前节点的深度为左右子树深度的最大值加 1
"""

from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            return max(left_depth, right_depth) + 1

        return dfs(root)
