class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        
        def backtrack(index,money):
            
            N = len(coins)

            if money > amount:
                return 0
            
            if money == amount:
                return 1
            
            if index >= N:
                return 0
       
            if (index,money) in cache:
            
                return cache[(index,money)]
            
            cache[(index,money)] = backtrack(index , money + coins[index]) + backtrack((index + 1),money)
            return cache[(index,money)]
                
        return backtrack(0,0)
        