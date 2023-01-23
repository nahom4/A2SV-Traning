class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check for each row and column first
        
        
        
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
              
                
                if board[i][j] in row:
                  
                    return False
                if board[i][j].isnumeric():
                
                    row.add(board[i][j])
        
                    
      
        
       
                    
        for i in range(len(board[0])):
            col = set()
         
            for j in range(len(board)):
                
                if board[j][i] in col:
                    return False
                if board[j][i].isnumeric():
                
                    col.add(board[j][i])
                    
        #let's check each 3X3 box
        for i in range(0,80,3):
          
            row = i//9
            col = i%9
            
         
            
            if row%3 == 0:
            
            
              
                
                new = set()
                
                for rw in range(row,row+3):
                   
                    for cl in range(col,col+3):
                        
                      
                    

                        if board[rw][cl] in new:
                            return False
                        if board[rw][cl].isnumeric():

                            new.add(board[rw][cl])
               
               
                
        return True

                    
                    
            
                    
 
        
        
        
                
            
                