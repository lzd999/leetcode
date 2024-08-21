"""
思路：
由题意可知，比较直观的做法是使用递归，先将左子树变为链表，再将右子树变为链表，
然后用临时变量暂存当前节点右子树，再让当前节点的左子树转到当前节点的右子树，再遍历右子树，找到修改后的最右侧节点，将该节点的右子树指向临时变量。
从示例 1 的输出可以得知最终结果和对二叉树的前序遍历非常相似，因此可以对当前二叉树进行前序遍历，
需要注意的是定义变量 pre 维护当前节点的上一个节点，
如果当前节点被访问过，则将其左子树置空，右子树指向当前节点，并修改 pre 指向当前节点即可。
"""

from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution114:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if node is None:
                return
            dfs(node.left)  # 将左子树变为链表
            dfs(node.right)  # 将右子树变为链表
            tmp = node.right  # 定义临时变量 tmp 暂存当前节点右子树
            node.right = node.left  # 让当前节点右子树指向当前节点左子树
            node.left = None  # 将左子树置空
            while node.right:  # 找到修改指向后的树的最右边
                node = node.right
            node.right = tmp  # 将临时变量维护的右子树接到修改后树的右边

        dfs(root)

        # if not root:
        #     return
        # pre = None
        # st = [(root, False)]
        # while st:
        #     node, visited = st.pop()
        #     if node is None:
        #         continue
        #     if not visited:
        #         st.append((node.right, False))
        #         st.append((node.left, False))
        #         st.append((node, True))
        #     else:
        #         if pre:
        #             pre.left = None
        #             pre.right = node
        #         pre = node
