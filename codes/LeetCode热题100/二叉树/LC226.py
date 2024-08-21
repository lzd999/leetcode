"""
思路：
1.递归
a.边界条件：当前节点为空，返回 None
b.递归过程：对当前节点的右子节点和左子节点调用递归函数，然后对当前节点的 left 和 right 重新赋值作交换
2.迭代
使用栈模拟递归过程：
a.将根节点入栈
b.从栈中取出一个节点，如果该节点的左右子节点存在，分别入栈，然后交换左右子节点
c.重复步骤 b 直至栈为空
"""

from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution226:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)

        # if not root:
        #     return None
        # st = []
        # st.append(root)
        # while st:
        #     node = st.pop()
        #     if node.left:
        #         st.append(node.left)
        #     if node.right:
        #         st.append(node.right)
        #     node.left, node.right = node.right, node.left
        # return root
