class Solution:
    def countOrders(self, n: int) -> int:
        cache = [0] * (n + 1)
        multi = [0] * (n + 1)
        if n == 1:
            return 1
        
        if n == 2:
            return 6
        
        cache[1] = 1
        cache[2] = 6
        multi[1] = 1
        multi[2] = 6
        
        
        
        for i in range(3,n + 1):
            diff = 2 * multi[i - 1] - multi[i - 2] + 4
            multi[i] = diff
            cache[i] = diff * cache[i - 1]
            
        return cache[n] % (10 ** 9 + 7)
            
        