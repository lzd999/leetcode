"""
144. 二叉树的前序遍历

给你二叉树的根节点 root ，返回它节点值的前序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
	树中节点数目在范围 [0, 100] 内
	-100 <= Node.val <= 100
进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import Optional, List

from leetcode.utils.tree_node import TreeNode


class Solution144:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(node):
        #     if node is None:
        #         return
        #     ans.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
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
                st.append((False, node.right))  # 右
                st.append((False, node.left))  # 左
                st.append((True, node))  # 根
            else:
                ans.append(node.val)
        return ans
