"""
思路：
本题属于组合型回溯
1.枚举选或不选左括号
a.当前操作：设当前括号序列的左括号数量为 left，枚举当前括号填左括号或右括号
b.子问题：构造括号数为 i，左括号数为 left 的括号序列
c.下一个子问题：构造括号数为 i+1，左括号数为 left+1 的括号序列
2.枚举选哪个
a.当前操作：设当前括号序列全是右括号，枚举其中哪些位置填左括号
b.子问题：构造括号数为 i 的括号序列，其中在 i+right 处填左括号
c.下一个子问题：构造长度为 i+1 的括号序列，其中在 i+right+1 处填左括号
"""

from typing import List


class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i, left):
            if i == m:
                ans.append("".join(path))
                return
            if left < n:
                path[i] = "("
                dfs(i + 1, left + 1)
            if left > i - left:
                path[i] = ")"
                dfs(i + 1, left)

        def dfs(i, diff):
            if len(path) == n:
                s = [')'] * m
                for j in path:
                    s[j] = '('
                ans.append(''.join(s))
                return
            for right in range(diff + 1):
                path.append(i + right)
                dfs(i + right + 1, diff - right + 1)
                path.pop()

        m = 2 * n
        ans = []
        path = [""] * m
        dfs(0, 0)
        return ans
