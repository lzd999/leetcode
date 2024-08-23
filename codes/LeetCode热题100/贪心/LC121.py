"""
思路：
本题求的是买卖股票过程中的最大利润，则需要遍历卖出价格 prices，
如果需要知道第 i 天的利润，就需要知道前 i-1 天的最低买入价格，然后用第 i 天的卖出价格减去最低买入价格，即可获得第 i 天的利润，
求这些利润中的最大值即可。
"""

from typing import List


class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans
