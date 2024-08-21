"""
思路：
先看示例 1，root = [3,5,1,6,2,0,8,null,null,7,4]
1.p=6,q=8
画出树后可以得知，p 的父节点是 5，q 的父节点是 1，而 5 和 1 分别是根节点 3 的左右子树，所以 p 和 q 的最近公共祖先是根节点 3
2.p=6,q=7
同理，p 的父节点是 5，q 的父节点是 2，2 的父节点是 5，所以 p 和 q 的最近公共祖先是节点 5
3.p=0,q=8
同理，p 和 q 的父节点是 1，所以 p 和 q 的最近公共祖先是节点 1
……
可以分类讨论：
1.如果当前节点为空，则返回 None
2.如果当前节点为 p 或者 q，则返回当前节点
3.如果 p 和 q 分别在左子树或右子树，则返回当前节点
4.如果 p 和 q 均在左子树或者右子树，则返回递归左子树或右子树的结果
5.如果 p 和 q 都不在当前节点的子树中，则返回 None
"""

from leetcode.utils.tree_node import TreeNode


class Solution236:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def dfs(node, p, q):
            # if node is None or node == p or node == q:
            if node in (None, p, q):
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right:
                return node
            return left or right

        return dfs(root, p, q)
