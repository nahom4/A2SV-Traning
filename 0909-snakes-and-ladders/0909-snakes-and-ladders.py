class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        forward = True
        lable = [[-1] * N for _ in range(N)]
        lableToPos = dict()
        currentLable = 1
         
        def buildForward(row):
            nonlocal currentLable
            for i in range(N):
                lable[row][i] = currentLable
                currentLable += 1
                
        def buildBackward(row):
            nonlocal currentLable
            for i in range(N -1 ,-1 ,-1):
                lable[row][i] = currentLable
                currentLable += 1
                
        def checkForSnakeOrLadder(lable):
            row,col = lableToPos[lable]
            if board[row][col] != -1:
                return True
                
        def addToQueue(pos):
            if not pos in visited:
                queue.append(pos)
                visited.add(pos)
            
            
        for i in range(N - 1,-1,-1):
            
            if forward:
                buildForward(i)
                forward = False
            else:
                buildBackward(i)
                forward = True
      
        for i in range(N):
            for j in range(N):
                lableToPos[lable[i][j]] = (i,j)
    
        queue = deque()
        queue.append((N - 1,0)) 
        visited = set()
        visited.add((N - 1,0))
        level = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                
                row,col = queue.popleft()
                value = board[row][col]
                posLable = lable[row][col]
                
                if posLable == N ** 2:
                    return level 
                
                for i in range(1,7):
                    posLable += 1
                    if posLable <= N ** 2:
                        row,col = lableToPos[posLable]
                        value = board[row][col]
                        if checkForSnakeOrLadder(posLable):
                            
                            pos = lableToPos[value]
                            addToQueue(pos)
                        else:
                            addToQueue((row,col))
                                      
            level += 1     
            
        return -1
            
                  
                    
            
                
        
            
        
        
        
       
        