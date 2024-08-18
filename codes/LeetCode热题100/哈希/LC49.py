"""
思路：
使用哈希表维护排序后的字符串与原字符串的映射关系。
"""

from collections import defaultdict
from typing import List


class Solution49:
    def groupAnagrams(self, ss: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in ss:
            mp["".join(sorted(s))].append(s)
        return list(mp.values())
