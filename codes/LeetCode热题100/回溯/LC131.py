"""
思路：
本题属于子集型回溯
观察示例 1，[["a","a","b"],["aa","b"]] 可以视为从第一个字符'a'开始，
先选第一个字符"a"，判断是否为回文串，是则加入回溯路径 ["a"]；
再选第二个字符"a"，判断是否为回文串，是则加入回溯路径 ["a","a"]；
再选第三个字符"b"，判断是否为回文串，是则加入回溯路径 ["a","a","b"]；
现在回溯路径长度为 3，可以将当前的回溯路径 ["a","a","b"] 加入答案；
然后弹出回溯路径的所有字符；
再选第一个和第二个字符 "aa"，判断是否为回文串，是则加入回溯路径 ["aa"]；
......
这种思路显然属于枚举选哪一个元素
a.当前操作：枚举当前子串的结束位置 j ∈ [i,n)，选择回文子串 s[i:j]，加入 path
b.子问题：当前回文子串的结束位置为 i
c.下一个子问题：当前回文子串的结束位置为 j+1
也可以枚举选或不选
示例 1 的答案也可以视为一个是选了字符串中间的第一个“间隙”和第二个“间隙”，另一个是只选了字符串中间的第二个“间隙”
a.当前操作：枚举选或不选 i 和 i+1 之间的间隙
b.子问题：当前回文子串的结束位置为 i
c.下一个子问题：当前回文子串的结束位置为 i+1 
"""

from typing import List


class Solution131:
    def partition(self, s: str) -> List[List[str]]:
        # def dfs(i, start):
        #     if i == n:
        #         ans.append(path.copy())
        #         return
        #     if i < n - 1:  # 不选 i 和 i+1 之间的间隙，i=n-1 必须要选
        #         dfs(i + 1, start)
        #     # 选 i 和 i+1 之间的间隙
        #     t = s[start: i + 1]
        #     if t == t[::-1]:  # 当前子串是回文串
        #         path.append(t)
        #         dfs(i + 1, i + 1)
        #         path.pop()

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i : j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        n = len(s)
        ans = []
        path = []
        # dfs(0, 0)
        dfs(0)
        return ans
