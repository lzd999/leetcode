"""
本题属于排列型回溯，从示例可以看出排列的长度是固定的，因此路径的长度也是固定的。
排列不同于组合，组合不能二次选取相同元素，但排列可以重复选取元素。
回溯过程中可以用一个布尔数组记录当前元素是否被使用过，是则跳过该元素。
"""

from typing import List


class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if not on_path[j]:
                    on_path[j] = True
                    path[i] = nums[j]
                    dfs(i + 1)
                    on_path[j] = False

        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n
        dfs(0)
        return ans
