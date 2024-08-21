"""
思路：
分别定义两个 cur 指向对应的 head，两个 cur 一起走，
在两个 cur 指向同一个节点之前，都需要先走完所在的当前链表后再从另一链表重新开始走，这期间经过的节点数量是相同的
"""

from typing import Optional
from leetcode.utils.list_node import ListNode

class Solution160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA
