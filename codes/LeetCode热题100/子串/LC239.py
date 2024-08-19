"""
思路：
最直接的思路是求每个滑动窗口的最大值，一共有 n-k+1 个滑动窗口，时间复杂度为 O(nk)，会超时，如何优化？
我们需要一种数据结构，它满足：
a.O(1) 能找到每个滑动窗口的最值 
b.方便移除滑动窗口的左边界元素和加入右边界元素
=> 使用队列维护每个滑动窗口的最值 => 单调队列
具体做法是：
a.每次将元素下标入队，当队列不为空时，比较当前元素与队尾元素大小，如果当前元素大于队尾元素则队尾元素弹出，直至当前元素小于队尾元素
b.当队内元素数量大于滑动窗口大小时，弹出队首元素
c.在 a. 不断操作后，队列元素呈单调递减，因此队列元素数量等于滑动窗口大小时，弹出队首元素，即当前滑动窗口最大值
※ 可以看出，单调栈 与 单调队列 同样是维护对应数据结构的单调性，区别在于单调队列需要多考虑移除队首元素操作，
    这和滑动窗口移动左边界是相似的，因此 单调队列 ≈ 单调栈 + 滑动窗口
"""

from collections import deque
from typing import List


class Solution239:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
