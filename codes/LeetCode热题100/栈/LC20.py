"""
思路：
题目涉及到括号匹配，一般做法是使用栈解决。
遍历当前字符串，遇到左括号则直接入栈，遇到右括号则判断栈顶元素是否为对应的左括号，不是则返回 False，相反则出栈。
最终判断栈是否为空，为空则返回 True，否则返回 False。
可以使用哈希表维护括号对应关系。
"""


class Solution20:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        st = []
        mp = {")": "(", "]": "[", "}": "{"}
        for cs in s:
            if cs not in mp:
                st.append(cs)
            elif not st or st.pop() != mp[cs]:
                return False
        return not st

        # n = len(s)
        # if n % 2 == 1:
        #     return False
        # st = []
        # for cs in s:
        #     if cs == "(":
        #         st.append(")")
        #     elif cs == "[":
        #         st.append("]")
        #     elif cs == "{":
        #         st.append("}")
        #     elif not st or st.pop() != cs:
        #         return False
        # return not st
