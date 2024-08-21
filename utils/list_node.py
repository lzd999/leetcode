class ListNode:
    """链表节点类"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list(self, nums: list):
        """创建链表"""
        if not nums:
            return None
        dummy = ListNode()
        cur = dummy
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next