"""
思路：
可以将 LRU缓存 想象成一摞书：
a.get 操作即把一本书抽出来，然后放回去
b.push 操作即放入一本新书，如果该书先前放过，则把它放到最上面，如果放上去的书的数量多于 capacity，则把最下面的书移除
为了满足题意，可以将一摞书用双向链表实现，每本书为双向链表的节点
定义 dummy 哨兵节点，不用特判节点为空的情况，且 dummy 的 next 指向最上面的一本书，prev 指向最后一本书
定义 key_node_map 字典，用于快速查找节点
1.get 操作：
a.如果 key 不存在，则直接返回
b.如果 key 存在，从双向链表中先抽出该节点，再插入到最前面，然后返回其 value
2.put 操作：
a.如果 key 存在，则更新 value，再将对应的节点移到最前面
b.如果 key 不存在，则根据 key 和 value 新建节点，再插入到最前面，
  每次 put 操作检查节点数量是否大于 capacity，如果是，则移除最后一个节点
"""

from typing import Optional


class Node:
    __slots__ = "prev", "next", "key", "val"

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_node_map = dict()

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, node: Node):
        node.prev = self.dummy
        node.next = self.dummy.next
        node.prev.next = node
        node.next.prev = node

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_node_map:
            return None
        node = self.key_node_map[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, val: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = val
            return
        node = Node(key, val)
        self.key_node_map[key] = node
        self.push_front(node)
        if len(self.key_node_map) > self.capacity:
            back_node = self.dummy.prev
            del self.key_node_map[back_node.key]
            self.remove(back_node)
