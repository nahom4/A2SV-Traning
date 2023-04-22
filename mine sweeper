class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def in_bound(pos):
            
            row,col = pos
            
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def count_mine(pos):
            
            count = 0
            r,c = pos
            for row in range(r - 1, r + 2):
                for col in range(c - 1,c + 2):
                    if (row,col) == pos:
                        continue
                        
                    if in_bound((row,col)) and board[row][col] == 'M':
                        count += 1
                        
            return count
                    
        def dfs(click):
            
            row,col = click
            
            if in_bound(click) and board[row][col] == 'M':
                board[row][col] = 'X'
                return
            
            if not in_bound(click) or board[row][col] != 'E':
                
                return
            
            count = count_mine(click)
            
            if count != 0:
                board[row][col] = str(count)
                return
            
            board[row][col] = 'B'
            
            for r in range(row - 1, row + 2):
                for c in range(col - 1,col + 2):
                    if (r,c) == (row,col):
                        continue
                        
                    dfs((r,c))
            
        dfs(tuple(click))
        return board
            
            
        