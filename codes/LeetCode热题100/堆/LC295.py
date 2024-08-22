"""
思路：
本题的实质就是给定一个长度为 N 的无序数组，计算该数组中位数。
最直观的做法是维护一个列表，每次添加一个数时，插入到列表尾部，每次取中位数时，对列表排序后返回中间元素。
显然，这种做法的时空复杂度都非常高，能否进行优化？
1.可以考虑使用有序列表，使用双指针表示当前有序列表中位数的左右两端，根据有序列表长度的奇偶性返回中位数。
2.也可以将有序列表抽象为一个三角形，三角形宽度表示元素大小，求中位数抽象为求三角形的中位线长度。
  将三角形按中位线切分后得到了一个梯形和一个倒三角形，结合三角形宽度的表示，可以发现，
  梯形可以表示最小堆，倒三角形可以表示最大堆，因此可以使用一个最大堆和一个最小堆来求中位数。
  具体做法是定义最大堆 max_hp 维护当前数组较小的一半，最小堆 min_hp 维护当前数组较大的一半，
  那么必然有最大堆和最小堆的元素数量差的绝对值不超过 1，
  每次添加一个数时，理论上是直接向最大堆添加，实际操作则是应先向最小堆添加，然后弹出最小堆的堆顶元素并加入最大堆，
  因为无法预知当前数的大小，可能属于较大的一半，也可能属于较小的一半，因此先向最小堆添加，再弹出堆顶元素，
  如果这个数属于最小堆，则弹出的堆顶元素必然属于最大堆；如果这个数属于最大堆，则堆进行调整后堆顶元素即为当前元素，同样达到向最大堆添加的目的。
"""

import heapq
from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        # self.ans = []

        # self.ans = SortedList()
        # self.left = self.right = None

        self.min_hp = []
        self.max_hp = []

    def addNum(self, num: int) -> None:
        # self.ans.append(num)

        # self.ans.add(num)
        # n = len(self.ans)
        # if n % 2 == 1:
        #     self.left = self.right = self.ans[n // 2]
        # else:
        #     self.left = self.ans[n // 2 - 1]
        #     self.right = self.ans[n // 2]

        m, n = len(self.min_hp), len(self.max_hp)
        if m != n:
            heapq.heappush(self.min_hp, num)
            heapq.heappush(self.max_hp, -heapq.heappop(self.min_hp))
        else:
            heapq.heappush(self.max_hp, -num)
            heapq.heappush(self.min_hp, -heapq.heappop(self.max_hp))

    def findMedian(self) -> float:
        # self.ans.sort()
        # n = len(self.ans)
        # if n % 2:
        #     return self.ans[n // 2] / 1
        # else:
        #     return (self.ans[n // 2 - 1] + self.ans[n // 2]) / 2

        # return (self.left + self.right) / 2.0

        return (
            self.min_hp[0]
            if len(self.min_hp) != len(self.max_hp)
            else (self.min_hp[0] - self.max_hp[0]) / 2
        )
