"""
思路：
Trie 树是一种用于存储字符串的多叉树，它会将字符串的每个字符存储在树节点。
每个 Trie 树节点的属性包括 children，用于指向下一个字符，is_end，用于判断是否为当前字符串的结尾。
1.插入操作：
从根节点开始，遍历当前字符串，不断将每个字符存储 Trie 树节点的 children 属性，
如果没有则创建一个新节点，并更新当前节点为该节点，直至当前节点为字符串最后一个字符，更新 is_end 为 True。
2.查找操作：
从根节点开始，遍历当前字符串，沿着 Trie 树节点的 children 属性不断匹配，
如果匹配到空节点或未匹配完，则返回 False，否则继续匹配下一个字符。
3.查找前缀操作：
从根节点开始，遍历当前前缀，沿着 Trie 树节点的 children 属性不断匹配，
如果匹配到空节点，则返回 False，否则返回 True。
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def searchPrefix(self, prefix: str) -> "TrieNode":
        node = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
