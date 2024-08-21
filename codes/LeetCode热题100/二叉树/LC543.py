"""
思路：
由题意可知，二叉树的直径可以转化为以当前节点为根节点时，其左子树和右子树的最大链长之和
1.递归
a.边界条件：当前节点为空，直径为 0
b.递归过程：先求以当前节点的左右子树为根节点的最大链长，取最大值后加 1，即为以当前节点为根节点的最大链长
  每次递归结束时，更新当前树的直径
"""

from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal ans
            ans = max(ans, left + right)
            return max(left, right) + 1

        ans = 0
        dfs(root)
        return ans
