class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        def pascalTriangle(level,numRows):
            
            if numRows == 1:
                return
            
            N = len(level) + 1
            currLevel = [0] * (N)
            currLevel[0] = 1
            currLevel[-1]  = 1
            for i in range(1,N - 1):
                currLevel[i] = level[i - 1] + level[i]
             
            ans.append(currLevel)
            numRows -= 1
            
            pascalTriangle(currLevel,numRows)
            
        pascalTriangle([1],numRows)
        return ans