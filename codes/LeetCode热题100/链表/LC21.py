"""
思路：
由于会对新链表的第一个节点进行修改，因此需要创建哨兵节点 dummy，
然后 l1 和 l2 同时遍历，每次比较 l1 和 l2 的值，将较小的节点连接到新链表的后面，然后指针向后移动，直至 l1 或 l2 其中一个为空。
最后将 l1 或 l2 不为空的部分直接连接到新链表的后面。
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution21:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
