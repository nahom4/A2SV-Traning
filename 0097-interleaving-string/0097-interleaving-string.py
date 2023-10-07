class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
       
        a,b,c = len(s1),len(s2),len(s3)
        if a + b != c:
            return False
        
        grid = [[False] * (a + 1) for _ in range(b + 1)]
         
        grid[0][0] = True
        for i in range(b + 1):
            for j in range(a + 1):
                
                if j - 1 >= 0 and s1[j - 1] == s3[j + i - 1]: #i = j = 1
                    grid[i][j] |= grid[i][j - 1]
        
                if i - 1 >= 0 and s2[i - 1] == s3[j + i - 1]:
                    grid[i][j] |= grid[i - 1][j]
                
        return grid[b][a]         
        
                
                
                
                
                
       
    
        