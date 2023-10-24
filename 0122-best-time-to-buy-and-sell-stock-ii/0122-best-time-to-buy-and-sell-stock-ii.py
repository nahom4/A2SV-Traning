class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        ans = 0
        for i in range(N - 1):
            if prices[i] < prices[i + 1]:
                ans += prices[i + 1] - prices[i]
                
        return ans
        