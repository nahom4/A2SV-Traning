class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        
#         lis = [-1] * (n + 1)
#         lis[0], lis[1] = 0,1
#         def getMax(n):
            
#             if n <= 1:
#                 return n
            
#             #even or odd
#             if n % 2 == 0:
#                 lis[n] = getMax(n // 2)
#                 return lis[n]
#             else:
#                 index = n - 1
#                 lis[n] = getMax(index // 2) + getMax(index // 2 + 1)
#                 return lis[n]
            
#         getMax(n)
#         print(lis)
#         return max(lis)
    
        #let's do bottom up
        if n < 2:
            return n
        lis = [-1] * (n + 1)
        lis[0], lis[1] = 0,1
        for index in range(n + 1):
            
            if index * 2 <= n:
                lis[index * 2] = lis[index]
            if index * 2 <= n  and index * 2 + 1 <= n:
                lis[index * 2 + 1] = lis[index + 1] + lis[index]
            
      
        return max(lis)
            
        