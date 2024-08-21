"""
思路：
观察示例 2 可知可能会对头节点进行操作 => 定义哨兵节点 dummy
核心是前后指针：定义 first 和 second，先让 first 移动 n 步，再让 first 和 second 一起移动，
通过 second 删除倒数第 n 个节点
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution19:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        first = second = dummy
        for _ in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
