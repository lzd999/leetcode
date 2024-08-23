"""
思路：
本题的要求是：「每个片段连续」，并且「每个片段不重叠」，并且「同一字母最多出现在一个片段中」，
这说明一个连续片段若包含一个字母，则当前连续片段必然包含该字母出现过的索引区间。
例如示例 1，s = ababcbacadefegdehijhklij，字母 a 的索引的所在区间是 [0,8]，则包含 a 的连续片段至少要包含 [0,8]。
不难发现，本题实质上就是 LC.56 合并区间 的变种。
定义哈希表 last 维护每个字符在字符串中最后一次出现的索引，定义 start 和 end 记录包含索引区间的左右端点，
遍历字符串，找到每个字符出现的索引区间右端点的最大值，如果某个字符右端点值正好等于当前遍历字符串位置，
说明该区间是一个连续片段，将该区间长度加入答案，同时令下一个连续片段的索引区间的左端点更新为当前右端点加 1。
"""

from typing import List


class Solution763:
    def partitionLabels(self, s: str) -> List[int]:
        last = {cs: i for i, cs in enumerate(s)}
        # last = dict()
        # for i, cs in enumerate(s):
        #     last[cs] = i
        ans = []
        start = end = 0
        for i, cs in enumerate(s):
            end = max(end, last[cs])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans
