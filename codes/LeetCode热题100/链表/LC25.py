"""
思路：
由于不知道链表节点个数是否为 k 的倍数，因此需要先统计节点个数 n
由于需要对第一个节点进行操作，因此需要设置哨兵节点 dummy
当前节点个数 ≥ k 时，对每 k 个节点组成的链表进行反转操作，在反转完成后，
由于后续需要修改 p0 的指向，因此要用临时变量 tmp 存储 p0 的下一个节点，
先让 tmp 指向 cur，再让 p0 指向 pre，最后修改 p0 为下一组链表头节点的上一个节点
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution25:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        dummy = ListNode(next=head)
        p0 = dummy
        pre, cur = None, head
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 由于后续需要调整 p0 的下一个节点，因此可以用 tmp 暂存当前 p0 的下一个节点（画图理解）
            tmp = p0.next # 暂存当前 p0 的下一个节点，本质上是翻转后链表的尾结点
            tmp.next = cur # 将尾结点指向 cur
            p0.next = pre # 修改翻转后链表的头节点 pre 为当前 p0 的下一个节点
            p0 = tmp # 将当前 p0 更新为下一段待反转链表的头结点的上一个节点
        return dummy.next
