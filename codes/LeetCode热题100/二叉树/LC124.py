"""
思路：
由题意可知，实质上是求树的所有直径中最大的链的元素和
可参考 LC543.二叉树的直径 的思路，当前节点为空则返回 0
否则先求左右子树的最大的链的元素和，再更新以当前节点为根节点拼成的链的元素和
然后返回当前子树的最大的链的元素和，注意节点值可能为负，如果加和为负则返回 0
"""

from typing import Optional
from math import inf
from leetcode.utils.tree_node import TreeNode


class Solution124:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            nonlocal ans
            ans = max(ans, left_val + right_val + node.val)
            return max(0, max(left_val, right_val) + node.val)

        ans = -inf
        dfs(root)
        return ans
