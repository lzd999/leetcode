"""
思路：
根节点可以不用判断，除此之外，对每个节点及其左右子树都要判断是否对称
即当前两个节点 p 和 q 本身的值是否相等，p 的左子树是否等于 q 的右子树，p 的右子树是否等于 q 的左子树，
三者均满足才能返回 True
1.递归
a.边界条件：p 和 q 均为空，返回 True，否则返回 False
b.递归过程：递归判断 p 的值是否等于 q 的值、p 的左子树是否等于 q 的右子树、p 的右子树是否等于 q 的左子树，
  如果三者都满足，则返回 True，否则返回 False
2.迭代
使用栈模拟递归过程
a.将根节点的左右子树入栈
b.取出栈顶的两个节点 p 和 q，如果均为空则继续，如果其中一个为空或者值不相等，返回 False，
  否则先将 p 的左子树和 q 的右子树入栈，再将 p 的右子树和 q 的左子树入栈
c.重复步骤 b，直至栈为空
"""

from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution101:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p or not q:
                return p == q
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)

        # st = [(root.left, root.right)]
        # while st:
        #     p, q = st.pop()
        #     if not p and not q:
        #         continue
        #     if not p or not q or p.val != q.val:
        #         return False
        #     st.append((p.left, q.right))
        #     st.append((p.right, q.left))
        # return True
