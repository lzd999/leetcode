"""
思路：
本题的思路和 LC.438 找到字符串中所有字母异位词 非常相似，
都是用滑动窗口维护所有子串，使用哈希表维护字符串计数，
当滑动窗口内的子串满足要求时，更新最小覆盖子串。
"""

from collections import Counter


class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)
        ans_l, ans_r = -1, ns
        cnt_t = Counter(t)
        cnt_s = Counter()
        left = 0
        for right, cs in enumerate(s):
            cnt_s[cs] += 1
            while cnt_s >= cnt_t:
                if right - left + 1 < ans_r - ans_l + 1:
                    ans_l, ans_r = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return s[ans_l : ans_r + 1] if ans_l >= 0 else ""
