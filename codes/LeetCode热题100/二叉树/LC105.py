"""
思路：
根据前序与中序遍历构建二叉树的思路是：
1.在前序遍历中找到根节点
2.在中序遍历中找到根节点所在位置
3.根据两个遍历中根节点的位置差得到左右子树的长度
4.递归建立左右子树
因此最直观的做法就是使用递归模拟这一思路即可。
优化：
a.可以使用哈希表预处理中序遍历，使得每次查找 preorder[0] 所在的位置减少到 O(1)
b.可以递归时并不传入前序和中序遍历的列表，而是直接传入区间，避免复制数组带来的额外开销
"""

from typing import List, Optional
from leetcode.utils.tree_node import TreeNode


class Solution105:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre_start, pre_end, in_start, in_end):
            if pre_start == pre_end:
                return None
            left_n = mp[preorder[pre_start]] - in_start
            left = dfs(pre_start + 1, pre_start + 1 + left_n, in_start, in_start + left_n)
            right = dfs(pre_start + 1 + left_n, pre_end, in_start + left_n + 1, in_end)
            return TreeNode(preorder[pre_start], left, right)

        mp = dict()
        for i, x in enumerate(inorder):
            mp[x] = i
        return dfs(0, len(preorder), 0, len(inorder))

        # if not preorder:
        #     return None
        # left_n = inorder.index(preorder[0])
        # left = self.buildTree(preorder[1 : left_n + 1], inorder[:left_n])
        # right = self.buildTree(preorder[left_n + 1 :], inorder[left_n + 1 :])
        # return TreeNode(preorder[0], left, right)
