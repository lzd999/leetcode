class TreeNode:
    """二叉树节点类"""

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def create_tree(self, nums):
        """创建二叉树"""
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.create_tree(nums[:mid])
        root.right = self.create_tree(nums[(mid + 1):])
        return root
