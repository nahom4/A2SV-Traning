class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        unchanged = []
        def dfs(pos):
         
            row,col = pos
            #check for 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            if board[row][col] == 'X':
                return
            #means hear it is an O so let's check if it is on the edge
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                self.valid = False
                
            board[row][col] = 'X'
            component.append(pos)
           
            for x,y in directions:
                dfs(((row + x),(col + y)))
            
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.valid = True
                component = []
            
                if board[row][col] == 'O':
                    dfs((row,col))
                   
                    if not self.valid:
                        unchanged.append(component)
                        
        #now let's apply the unchanged values to the board
        for lis in unchanged:
            for pos in lis:
                row,col = pos
                board[row][col] = 'O'
                
        return board