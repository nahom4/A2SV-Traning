class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = {}
        def dp(sm):
            
            if sm == amount:
                return 0
            
            if sm > amount:
                return float('inf')
            
            if sm in cache:
                return cache[sm]
            min_num_coins = float('inf')
            for coin in coins:
                min_num_coins = min(1 + dp(sm + coin),min_num_coins)
                
            cache[sm] = min_num_coins
                
            return min_num_coins
        result = dp(0)
        return -1 if result == float('inf') else result
        