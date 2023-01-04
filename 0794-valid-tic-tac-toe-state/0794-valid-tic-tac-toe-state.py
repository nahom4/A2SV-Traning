import numpy
class Solution:
    
    def checkWinner(self,board,char):
        
        #row check
        for row in board:
            result = all([char== n for n in row])
            if result:
                return result
        # column check
     
        for col in range(3):
            lis=[]
            for row in range(3):
                lis.append(board[row][col] == char)

            if all(lis):
                return True
                
                
            
          
            
        # diagonal check
        #we have to check two diagonals from 00 right diagonal from 02 left diagonal
        lis = []
        for i in range(3):
            for j in range(i,3):
                lis.append(char == board[i][j])
                break
        if all(lis):
            return True
        lis = []
        for m in range(2,-1,-1):
            for n in range(2-m,-1,-1):
                lis.append(board[m][n]==char)
                break
        if all(lis):
            return True
                
                    
            
        
        
        
        
    def validTicTacToe(self, board: List[str]) -> bool:
        
        #number of x is greater or equal to number of o
        
        x = 0
        o= 0
        
        for row in board:
            for value in row:
                if value == "X":
                    x+=1
                elif value =="O":
                    o+=1
                
                

        if x-o == 0 or x-o ==1:
          
            if self.checkWinner(board,'O') and self.checkWinner(board,'X'):
                return False
            if self.checkWinner(board,'O') and x-o ==1:
                return False
            if self.checkWinner(board,'X') and  x-o == 0:
                return False
            if x + o ==9:
                return x-o ==1
              
            return True
                
                
        else:
            return False
                
        