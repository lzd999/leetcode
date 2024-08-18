"""
思路：
使用滑动窗口维护 s 的所有子串；
使用哈希表维护当前子串是否出现重复字符；
遍历 s，如果当前滑动窗口内出现重复字符，则移动滑动窗口左边界；
否则将当前字符加入哈希表，并更新最大长度
"""

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        s_set = set()
        left = 0
        for right, cs in enumerate(s):
            while cs in s_set:
                s_set.remove(s[left])
                left += 1
            s_set.add(cs)
            ans = max(ans, right - left + 1)
        return ans
