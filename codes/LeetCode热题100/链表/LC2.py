from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0 # 进位
        while l1 or l2 or carry != 0:
            carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

        