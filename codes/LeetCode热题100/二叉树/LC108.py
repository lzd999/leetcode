"""
思路：
二叉搜索树的中序遍历一定是严格递增的，而数组 nums 同样严格递增，
因此本题的实质是根据二叉搜索树的中序遍历还原二叉搜索树
最直观的方法是使用递归和二分的思想还原二叉搜索树
"""

from typing import List, Optional
from leetcode.utils.tree_node import TreeNode


class Solution108:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(nums, left, mid - 1)
            node.right = build_tree(nums, mid + 1, right)
            return node

        n = len(nums)
        return build_tree(nums, 0, n - 1)
