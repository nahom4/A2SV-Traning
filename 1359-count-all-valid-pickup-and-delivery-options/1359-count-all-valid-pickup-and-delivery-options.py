class Solution:
    def countOrders(self, n: int) -> int:
        #bottom up
        cache = [0] * n
        cache[0] = 1
        slot = 3
        Mod =  (10 ** 9 + 7)
        for i in range(2,n + 1):
            cache[i - 1] = cache[i - 2] * (slot + 1) * slot // 2
            slot += 2
            
        return cache[n - 1] % Mod
            
        