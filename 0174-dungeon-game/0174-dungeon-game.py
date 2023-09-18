class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if not dungeon:
            return 0

        N = len(dungeon)
        M = len(dungeon[0])

        # Create a 2D cache to store the minimum required strength for each cell
        cache = [[0] * M for _ in range(N)]

        def dp(row, col):
            if row == N - 1 and col == M - 1:
                return max(1, 1 - dungeon[row][col])

            if cache[row][col] > 0:
                return cache[row][col]

            # Calculate the minimum required strength for moving right and moving down
            rightMinReq = float('inf') if col == M - 1 else dp(row, col + 1)
            downMinReq = float('inf') if row == N - 1 else dp(row + 1, col)

            # Calculate the minimum required strength to reach this cell
            minReq = min(rightMinReq, downMinReq) - dungeon[row][col]

            # Ensure the minimum required strength is at least 1
            minReq = max(1, minReq)

            cache[row][col] = minReq
            return minReq

        return dp(0, 0)


    
#         #let's turn the recursive solution into an itetrative one
      
#         N = len(dungeon)
#         M = len(dungeon[0])
#         cache = [[1] * M for _ in range(N)]
#         strength = [[0] * M for _ in range(N)]
#         def getNoSheild(pos):
#             row,col = pos
#             if not(0 <= row < N ) or not(0 <= col < M):
#                 return 0
            
#             return cache[row][col]
#         def getStrength(pos):
#             row,col = pos
#             if not(0 <= row < N ) or not(0 <= col < M):
#                 return 0

#             return strength[row][col]
#         for row in range(N - 1,-1,-1):
#             for col in range(M - 1,-1,-1):
#                 rightStrength = getStrength((row , col + 1))  + dungeon[row][col]
#                 leftStrength = getStrength((row + 1 , col))  + dungeon[row][col]
                
#                 rightMinReq = getNoSheild((row , col + 1))
#                 leftMinReq = getNoSheild((row + 1 , col))
                
#                 if rightMinReq < leftMinReq:
                     
#                     if rightStrength <= 0:
#                         noSheild = -(rightStrength) + 1
#                         rightStrength = 1
                        
#                     elif rightStrength > 0:
#                         noSheild = -(rightStrength - 1)
#                         rightStrength = 1
                        
#                     currStrength = rightStrength
#                     res = rightMinReq + noSheild
#                 else:
#                     if leftStrength <= 0:
#                         noSheild = -(leftStrength) + 1
#                         leftStrength = 1
                        
#                     elif rightStrength > 0:
#                         noSheild = -(leftStrength - 1)
#                         leftStrength = 1
                    
#                     currStrength = leftStrength
#                     res =  leftMinReq + noSheild
                   
#                 print((row,col),res)
#                 cache[row][col] = res
#                 strength[row][col] = currStrength
                
#         print(cache)
#         return cache[0][0]
                
                
            
                
                

        

            
            