"""
思路：
1.递归
根据中序遍历访问当前节点的顺序：左 -> 根 -> 右，依次访问，边界条件为当前节点为空节点。
2.迭代
使用栈模拟中序遍历访问节点，由于栈是后进先出，因此入栈的顺序为：右 -> 根 -> 左。
"""

from typing import List, Optional
from leetcode.utils.tree_node import TreeNode


class Solution94:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans

        # ans = []
        # st = [(False, root)]
        # while st:
        #     visited, node = st.pop()
        #     if node is None:
        #         continue
        #     if not visited:
        #         st.append((False, node.right))  # 右
        #         st.append((True, node))  # 根
        #         st.append((False, node.left))  # 左
        #     else:
        #         ans.append(node.val)
        # return ans
