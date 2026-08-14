class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        ans = 0

        for price in prices:
            ans = max(ans, price - minPrice)
            minPrice = min(minPrice, price)

        return ans