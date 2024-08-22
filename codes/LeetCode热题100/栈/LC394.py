"""
思路：
由于本题涉及到中括号匹配，必然使用栈，难点在于如何通过栈实现中括号的嵌套匹配。
遍历当前字符串：
1.如果遇到数字，则将当前数字转化为乘数，注意多位数的处理，例如 34[a]。
2.如果遇到字母，则直接加入答案。
3.如果遇到左括号，则将当前字符串和乘数入栈，然后重置当前字符串和乘数。
4.如果遇到右括号，则弹出栈顶元素，并根据栈顶元素存储的字符串和乘数，生成新的字符串。
"""


class Solution394:
    def decodeString(self, s: str) -> str:
        ans = ""
        st = []
        multi = 0
        for cs in s:
            if cs.isdigit():
                multi = multi * 10 + int(cs)
            elif cs.isalpha():
                ans += cs
            elif cs == "[":
                st.append((ans, multi))
                ans, multi = "", 0
            elif cs == "]":
                top = st.pop()
                ans = top[0] + ans * top[1]
        return ans
