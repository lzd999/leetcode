"""
思路：
为了方便合并，可以先按照每个区间的左端点排序
排序后就可以知道第一个待合并区间的左端点，但第一个待合并区间的右端点是什么还不清楚，可能不变，可能被后续区间合并
可以先将第一个合并区间加入答案，表示当前待合并区间
遍历第二个待合并区间，如果第二个合并区间的左端点小于等于当前待合并区间的右端点，说明两个区间可以合并，更新当前待合并区间的右端点
否则说明当前区间已合并完成，遍历下一个合并区间
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for p in intervals:
            start, end = p[0], p[1]
            if ans and start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append(p)
        return ans
