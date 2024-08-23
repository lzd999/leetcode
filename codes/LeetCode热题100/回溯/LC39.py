"""
思路：
本题属于组合型回溯，一般的形式是在 n 个数里选 k 个数进行组合，相当于长度固定的子集
思路同样适用，即枚举选或不选和枚举选哪个
1.枚举选或不选
a.当前操作：设当前枚举的元素为 nums[i]，剩余待选的元素和为 s，枚举选或不选 nums[i]
b.子问题：构造前 i 个元素的组合，剩余待选元素和为 s
c.下一个子问题：构造前 i+1 个元素的组合，剩余待选元素和为 s-nums[i]
2.枚举选哪个
a.当前操作：枚举选 nums[j]，j ∈ [i,n)
b.子问题：构造前 i 个元素的组合，剩余待选元素和为 s
c.下一个子问题：构造前 i+1 个元素的组合，剩余待选元素和为 s-nums[j]
"""

from typing import List


class Solution39:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # def dfs(i, s):  # s 表示剩余未被选择的元素和
        #     if s == 0:
        #         ans.append(path.copy())
        #         return
        #     if i == n or s < nums[i]:
        #         return
        #     dfs(i + 1, s)  # 不选，则 s 不变
        #     path.append(nums[i])
        #     dfs(i, s - nums[i]) # 选，则 s 减去 nums[i]
        #     path.pop()

        def dfs(i, s):
            if s == 0:
                ans.append(path.copy())
                return
            if s < nums[i]:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j, s - nums[j])
                path.pop()

        n = len(nums)
        nums.sort()
        ans = []
        path = []
        dfs(0, target)
        return ans
