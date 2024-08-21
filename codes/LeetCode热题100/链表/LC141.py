"""
思路：
快慢指针
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution141:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
