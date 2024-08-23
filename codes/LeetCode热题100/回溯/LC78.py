"""
思路：
本题属于子集型回溯，对子集型回溯，一般有两种思路：
1.站在输入的角度，枚举选或不选当前元素
2.站在答案的角度，枚举选哪一个元素
回到本题，两种思路均可采用
1.枚举选或不选
当前操作：枚举选或不选 nums[i]
子问题：构造前 i 个元素组成的子集
下一个子问题：构造前 i+1 个元素组成的子集
2.枚举选哪一个元素
当前操作：枚举选第 j 个元素，j ∈ [i, n)
子问题：构造前 i 个元素组成的子集
下一个子问题：构造前 i+1 个元素组成的子集
"""

from typing import List


class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 枚举选或不选
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        # 枚举选哪一个元素
        # def dfs(i):
        #     ans.append(path.copy()) # 递归前将已选元素组成的集合加入答案
        #     if i == n:
        #         return
        #     for j in range(i, n):
        #         path.append(nums[j])
        #         dfs(j + 1)
        #         path.pop()

        n = len(nums)
        ans = []
        path = []
        dfs(0)
        return ans
