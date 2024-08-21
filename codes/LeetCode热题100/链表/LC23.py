"""
思路：
对由多个链表组成的数组升序排序，一般都是采用归并排序
如果当前数组没有链表，则返回 None；
如果当前数组仅有一个链表，则返回该链表；
否则，先将数组先拆分为左右两部分，再分别对左右两部分递归排序，最后将左右两部分合并。
"""

from typing import List, Optional
from leetcode.utils.list_node import ListNode


class Solution23:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1, l2):
            cur = dummy = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return dummy.next

        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        left = self.mergeKLists(lists[: k // 2])
        right = self.mergeKLists(lists[k // 2 :])
        return mergeTwoLists(left, right)
