class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        #let's try bottom up dp
        N = len(dungeon)
        M = len(dungeon[0])
        prefix = [[0] * M for _ in range(N)]
        
        def getPrevValue(pos):
            row,col = pos
            
            if not ( 0 <= row < N) or not (0 <= col < M):
                return float("-inf")
            
            return prefix[row][col]
        
        target = dungeon[N - 1][M - 1]
        prefix[N -1][M - 1] = target if target < 0 else 0
        for i in range(N - 1,-1,-1):
            for j in range(M - 1,-1,-1):
                
               
                if (i,j) == (N - 1, M - 1):
                    continue
                    
                rightPath = getPrevValue((i,j + 1))
                downPath = getPrevValue((i + 1,j))
                
                currValue = dungeon[i][j] + max(rightPath,downPath)
                
                if currValue >= 0:
                    prefix[i][j] = 0
                    
                else:
                    prefix[i][j] = currValue
           
        return 1 if prefix[0][0] > 0 else -prefix[0][0] + 1
                
                
                
                
        