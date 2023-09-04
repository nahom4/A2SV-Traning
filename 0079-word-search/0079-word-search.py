class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
    
        BN = len(board)
        BM = len(board[0])
        visited = set()
        def inBound(pos):
            row,col = pos
            
            return 0 <= row < BN and 0 <= col < BM
        def backTrack(pos,i,word):
            N = len(word)
            row,col = pos
            if i == N - 1 and board[row][col] == word[i]:
                
                return True
            
            valid = False
            for x,y in direction:
                nxtCoord = (x + row,y + col)
                if inBound(nxtCoord)  and i + 1  < N and board[nxtCoord[0]][nxtCoord[1]] == word[i + 1] and not nxtCoord in visited:

                    visited.add(nxtCoord)
                    valid = valid or backTrack(nxtCoord,i + 1,word)
                    visited.remove(nxtCoord)
                    
            return valid
        
        def isWordInBoard(word):
          
            startPos = []
            startLetter = word[0]
            for row in range(BN):
                for col in range(BM):
                    if board[row][col] == startLetter:
                        startPos.append((row,col))
             
            valid = False
            for pos in startPos:
                visited.add(pos)
                valid = valid or backTrack(pos,0,word)
                visited.remove(pos)
                if valid:
                    return valid
            
            return valid
        
        return isWordInBoard(word)