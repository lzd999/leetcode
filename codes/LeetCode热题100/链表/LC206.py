"""
思路：
遍历当前链表
定义 pre 指向 null，cur 指向 head
每次遍历，先定义 nxt 指向 cur 的下一个节点，再将 cur 的下一个节点指向 pre，
然后移动 pre 和 cur 指针到下一个节点
最终 pre 指向反转后的链表头节点，cur 指向反转后链表头节点的下一个节点
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution206:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

        # def dfs(pre, cur):
        #     if not cur:
        #         return pre
        #     res = dfs(cur, cur.next)
        #     cur.next = pre
        #     return res
        # 
        # return dfs(None, head)