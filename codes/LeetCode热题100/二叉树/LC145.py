"""
145. 二叉树的后序遍历

给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

提示：
	树中节点的数目在范围 [0, 100] 内
	-100 <= Node.val <= 100
进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import Optional, List

from leetcode.utils.tree_node import TreeNode


class Solution145:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(node):
        #     if node is None:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)
        #     ans.append(node.val)
        #
        # ans = []
        # dfs(root)
        # return ans

        ans = []
        st = [(False, root)]
        while st:
            visited, node = st.pop()
            if node is None:
                continue
            if not visited:
                st.append((True, node))  # 根
                st.append((False, node.right))  # 右
                st.append((False, node.left))  # 左
            else:
                ans.append(node.val)
        return ans
