"""
思路：
本质是 LC25 k = 2 的情况
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution24:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        dummy = ListNode(next=head)
        p0 = dummy
        pre, cur = None, head
        while n >= 2:
            n -= 2
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            tmp = p0.next
            tmp.next = cur
            p0.next = pre
            p0 = tmp
        return dummy.next
