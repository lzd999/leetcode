"""
思路：
最直接的做法是访问每一个节点，计算以当前节点为根节点且路径元素和为 targetSum 的路径数量：
定义 dfs(node, s) 表示以 node 为根节点时当前路径元素和为 s，
然后对当前节点及其左右子树进行判断其路径是否满足，满足则加入答案。
怎么优化呢？
可以发现，暴力做法里必然会产生重复计算，因此可参考 LC560.和为 K 的子数组，
定义当前节点的前缀和为从根节点开始到当前节点的路径上所有节点的元素和
使用哈希表统计前缀和与 targetSum 相减的出现次数
遍历每个节点，设从根节点开始到当前节点的路径元素和为 s，如果找到了 cnt[s - targetSum] 个路径，则加入答案
"""

from typing import Optional
from collections import defaultdict
from leetcode.utils.tree_node import TreeNode


class Solution437:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if node is None:
                return
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1

        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        dfs(root, 0)
        return ans

        # def dfs(node, s):
        #     if node is None:
        #         return 0
        #     res = 0
        #     if node.val == s:
        #         res += 1
        #     res += dfs(node.left, s - node.val)
        #     res += dfs(node.right, s - node.val)
        #     return res
        #
        # if root is None:
        #     return 0
        # ans = dfs(root, targetSum)
        # ans += self.pathSum(root.left, targetSum)
        # ans += self.pathSum(root.right, targetSum)
        # return ans
