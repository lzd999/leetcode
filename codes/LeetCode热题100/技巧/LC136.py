"""
思路：
异或运算的性质：a ^ a = 0, a ^ 0 = a
我们可以利用异或运算这一性质，将数组中所有数字异或，最后得到的结果就是只出现一次的数字。
"""

from typing import List


class Solution136:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
