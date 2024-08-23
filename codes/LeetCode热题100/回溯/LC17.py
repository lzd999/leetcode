"""
思路：
※ 只要题目出现了类似“返回所有可能的方案”的提示，一般都可以使用回溯解题。
※ 如果当前题目能使用回溯，可以画出解题过程表示的辅助树结构，
按照使用回溯解题的思路：将初始状态视作根节点，将每次选择产生的所有子状态视作中间节点，将所有选择完成后的最终状态视作叶节点。
回到本题，
1.题目出现了【返回所有它能表示的字母组合】，考虑使用回溯解题。
2.可预定义哈希表维护数字与字母的映射关系，然后枚举 digits 字符串的每个数字，根据哈希表获取当前数字对应的所有字母，将每个数字对应的所有字母进行穷举，得到所有方案。
  体现在代码上就是用 path 记录当前路径，每次枚举 digits 的一个数字，先用哈希表查找对应的所有字母，
  再将当前选择的字母加入路径，将这一过程封装成 dfs 函数并递归调用，直到当前路径长度等于 digits 长度，说明已经选择了所有数字，
  再将路径加入答案。
可以看出，回溯的本质是穷举所有可能，然后筛选出符合要求的方案。
"""

from typing import List


class Solution17:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            for cs in MAPPING[digits[i]]:
                path[i] = cs
                dfs(i + 1)

        MAPPING = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        ans = []
        if n == 0:
            return ans
        path = [""] * n
        dfs(0)
        return ans
