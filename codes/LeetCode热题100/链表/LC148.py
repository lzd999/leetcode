"""
思路：
一般对链表排序都是先将链表转化为数组，再对数组排序，最后还原为链表
但题目要求时间复杂度为 O(nlogn)，空间复杂度为 O(1)，因此可以考虑归并排序，
如果是对数组使用归并排序，空间复杂度为 O(n)，时间复杂度为开辟新数组 O(n) + 递归函数调用 O(logn)
链表的优质在于可以通过修改引用来更改节点顺序，无需开辟额外空间。
但如果选择递归仍会产生 O(logn) 的空间复杂度，因此需要考虑迭代的归并排序
具体做法如下：
1.统计链表的节点数量 n，用于与单元长度 intv 比较是否完成排序
2.创建哨兵节点 dummy，指向 head，用于：
  a.每一轮合并时，可通过哨兵节点找到合并后的头节点
  b.每一次排序合并时，作为链表头部排序时的辅助
3.每一轮合并：
  a.根据当前单元长度 intv 找到合并单元 1 和合并单元 2 的头部 h1 和 h2，
    ※ 如果 h2 存在，但合并单元 2 的元素数量少于 intv，也执行合并，且合并单元 2 的元素数量为 intv - i
    ※ 如果 h2 不存在，则无需合并，直接 break
  b.合并长度为 c1 和 c2 的合并单元 1 和合并单元 2
  c.合并完成后修改新的合并单元尾部，指向下一个合并单元头部，当 h 为 None，说明当前轮合并已结束，开始下一轮
"""

from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution148:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        dummy = ListNode(next=head)
        intv = 1
        while intv < n:
            pre, cur = dummy, dummy.next
            while cur:
                h1, i = cur, intv
                while i and cur:
                    i -= 1
                    cur = cur.next
                if i:
                    break
                h2, i = cur, intv
                while i and cur:
                    i -= 1
                    cur = cur.next
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = cur
            intv *= 2
        return dummy.next

        # nums = []
        # cur = head
        # while cur:
        #     nums.append(cur.val)
        #     cur = cur.next
        # nums.sort()
        # cur = head
        # for x in nums:
        #     cur.val = x
        #     cur = cur.next
        # return head
