"""
思路：
1.最直观的做法是利用二叉搜索树的中序遍历是严格递增数组这一性质，
对二叉搜索树进行中序遍历，然后返回第 k 个元素即可
2.题目中出现"...第 k 小..."的字眼，可以考虑使用堆
创建一个大小为 k 的大根堆，对当前二叉搜索树进行中序遍历，将每个节点对应值放入大根堆，
将前 k-1 个元素出堆后，堆顶元素即为答案
"""

import heapq
from typing import Optional
from leetcode.utils.tree_node import TreeNode


class Solution230:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans = []
        # st = [(root, False)]
        # while st:
        #     node, visited = st.pop()
        #     if node is None:
        #         continue
        #     if not visited:
        #         st.append((node.right, False))
        #         st.append((node, True))
        #         st.append((node.left, False))
        #     else:
        #         if k == 0:
        #             break
        #         ans.append(node.val)
        #         k -= 1
        # return ans[-1]

        st = [(root, False)]
        hp = []
        while st:
            node, visited = st.pop()
            if node is None:
                continue
            if not visited:
                st.append((node.right, False))
                st.append((node.left, False))
                st.append((node, True))
            else:
                if len(hp) < k:
                    heapq.heappush(hp, -1 * node.val)
                elif -1 * hp[0] > node.val:
                    heapq.heappop(hp)
                    heapq.heappush(hp, -1 * node.val)
        return -1 * hp[0]
