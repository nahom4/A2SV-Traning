class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        cache = {}
        Mod = ( 10 ** 9 + 7)
        def dp(sm,i):
            
            if sm == 0:
                return 1
            
            if i > n:
                return 0
            
            nm = i ** x % Mod
            if nm > sm:
                return 0
            if (sm,i) in cache:
                return cache[(sm,i)]
            
            
            
            count = dp(sm - nm, i + 1) + dp(sm, i + 1)
            cache[(sm,i)] = count
            return count
        
        return dp(n,1) % Mod
    
#         cache = defaultdict(int)
#         limit = int(n ** (1 / x))
#         cache[(0,0)] = 1
#         for amount in range(n,-1,-1):
#             count = 0
#             for num in range(1,limit):
#                 count += cache[(amount - (num ** x),num - 1)]
#                 cache[(amount,num)] = count
               
#         return cache[(amount,limit)] % ( 10 ** 9 + 7)
        
            
        