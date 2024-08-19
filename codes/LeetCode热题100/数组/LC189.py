"""
思路：
最直观的做法就是创建一个额外数组，用于缓存原数组，向右轮转 k 个位置即为 (i+k) % n（注意 k 可能大于 n）
如果需要减少空间复杂度，则只能在原数组上修改，同样注意 k 和 n 的取值
使用双指针：
1.对整个数组进行翻转
2.对前 k 个元素进行翻转
3.对后 n-k 个元素进行翻转
"""
from typing import List


class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # cache = nums.copy()
        # for i in range(n):
        #     nums[(i + k) % n] = cache[i]

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)