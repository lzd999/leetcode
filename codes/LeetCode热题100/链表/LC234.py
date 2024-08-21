"""
思路：
先使用快慢指针找到当前链表的中间节点 mid，
再将链表翻转找到后半链表的头节点 h2
最后 h1 和 h2 同时移动，只要出现节点值不相等则返回 False，否则返回 True
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution234:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middleNode(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(head):
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        mid = middleNode(head)
        h1, h2 = head, reverseList(mid)
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True

        # 这种方法为什么不对？
        # 因为虽然对 head 做了翻转操作，但 head 的指针没有变，所以 p1, p2 的指针均指向同一个链表！！!
        # p1, p2 = head, reverseList(head)
        # while p1:
        #     if p1.val != p2.val:
        #         return False
        #     p1 = p1.next
        #     p2 = p2.next
        # return True
