"""
思路：
由题意可知，p 是否是 s 某个子串的 “异位词” 取决于当前子串包含的每个字符和数量是否与 p 相等。
显然可以使用滑动窗口维护 s 的每个子串，使用哈希表维护 p 和 s 子串的字符及对应数量。
遍历 s；
将 s 的每个字符加入哈希表；
如果当前滑动窗口内的字符数量大于 p 的数量，说明一定不是 p 的异位词，移动滑动窗口左边界；
如果当前滑动窗口长度等于 p 的长度，说明当前子串必然是 p 的异位词，则将当前子串的起始位置加入答案；
"""

from collections import Counter
from typing import List


class Solution438:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        ans = []
        cnt_p = Counter(p)
        cnt_s = Counter()
        left = 0
        for right, cs in enumerate(s):
            cnt_s[cs] += 1
            while cnt_s >= cnt_p:
                if right - left + 1 == np:
                    ans.append(left)
                cnt_s[s[left]] -= 1
                left += 1
            # 优化：当滑动窗口内的字符数量大于 p 的数量时，移动滑动窗口左边界
            # while cnt_s[cs] > cnt_p[cs]:
            #     cnt_s[s[left]] -= 1
            #     left += 1
            # if right - left + 1 == np:
            #     ans.append(left)
        return ans
