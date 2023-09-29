class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minValue = float("inf")
        N = len(prices)
        profit = 0
        for i in range(N):
            if prices[i] > minValue:
                profit = max(profit,prices[i] - minValue)
                
            minValue = min(minValue,prices[i])
            
        return profit
            
        