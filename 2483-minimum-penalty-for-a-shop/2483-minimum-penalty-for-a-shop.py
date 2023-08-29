class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        N = len(customers)
        ans = [0] * N
        
        count = 0
        for i in range(N):
            
            ans[i] += count
            if customers[i] == 'N':
                count += 1
                
        count = 0
        for i in range(N - 1,-1,-1):
            
            if customers[i] == 'Y':
                count += 1
                
            ans[i] += count
           
        ans.append(customers.count('N'))
        return ans.index(min(ans))
            
            
                    
        