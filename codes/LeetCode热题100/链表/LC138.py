"""
思路：
给定链表头节点，复制一个新链表，通常只需要遍历链表，构建当前节点 cur 和前驱节点 pre 的引用即可，
但本题节点还有 random 属性用于存储当前节点在链表转化成数组后的所在位置，而链表无法进行随机访问，
因此难点在于如何在复制链表的同时提前知道每个节点在链表的位置
1.哈希表
使用哈希表维护新节点与原节点的映射关系，第一次遍历链表仅映射对应值，同时也知道了每个节点的 random 是否被创建了，
第二次遍历链表，将当前节点的 next 映射到新节点的 next，同时将当前节点的 random 映射到新节点的 random
2.原地复制
可在原有链表的基础上对每个节点复制后进行拼接，生成类似 1 -> 1' -> 2 -> 2' -> 3 -> 3' ...... 的链表
"""

from typing import Optional


class Node(object):
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution138:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return
        # mp = dict()
        # cur = head
        # while cur:
        #     mp[cur] = Node(cur.val)  # 构建旧节点到新节点的映射关系
        #     cur = cur.next
        # cur = head
        # while cur:
        #     mp[cur].next = mp.get(cur.next)
        #     mp[cur].random = mp.get(cur.random)
        #     cur = cur.next
        # return mp[head]

        cur = head
        while cur:
            cur2 = Node(cur.val)  # 对当前原节点复制生成新节点
            cur2.next = cur.next  # 修改新节点的下一个节点为下一个原节点
            cur.next = cur2  # 修改当前原节点的下一个节点为新节点，表示将新节点插入当前原节点和下一个原节点之间
            cur = cur2.next  # 移动当前原节点到下一个原节点
        # 最终生成的链表，每个节点都有两个节点，第一个节点是原节点，第二个节点是新节点
        cur = head
        while cur:
            if cur.random:  # 发现当前原节点的 random 不为 null
                cur.next.random = cur.random.next  # 将新节点的 random 修改为原节点的 random 的所示位置
            cur = cur.next.next
        # 将拼接链表拆分成两个链表：原节点链表、新节点链表
        pre = head
        cur = ans = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 原链表的尾节点单独处理
        return ans
