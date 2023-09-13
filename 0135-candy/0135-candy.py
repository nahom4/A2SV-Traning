class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        #go forward and backward
        N = len(ratings)
        ans = [1] * (N)
       
        for i in range(1,N):
            if ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1
                
                
        for i in range(N - 2,-1,-1):
            if ratings[i] > ratings[ i + 1]:
                ans[i] = max(ans[i],ans[i + 1] + 1)
                
                
        return sum(ans)
            
            