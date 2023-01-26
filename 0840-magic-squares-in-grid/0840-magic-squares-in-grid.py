class Solution:
    def distinct(self,i,index,grid):
        
        
        
        repeat = set()
        for m in range(i,i+3):
            for n in range(index,index+3):
                if not grid[m][n] in repeat and 1<= grid[m][n]<=9:
                    repeat.add(grid[m][n])
                else:
                    return False
                
     
        return True
        
        
        
    
    def check(self,i,index,grid):
        #row 
        repeat = set()
        sm  = 0
        for m in range(i,i+3):
            for n in range(index,index+3):
                sm+= grid[m][n]
            repeat.add(sm)
            sm = 0
            if len(repeat) > 1:
                return False
             
        #col
        repeat = set()
        for n in range(index,index+3):
            for m in range(i,i+3):
                sm+= grid[m][n]
            repeat.add(sm)
            sm = 0
            if len(repeat) > 1:
                return False

             
        #left diagonal
        sm = sum([grid[i][index],grid[i+1][index+1],grid[i+2][index+2]])
        repeat.add(sm)
        
        if len(repeat) > 1:
            return False
        
        #right diagonal
        sm = sum([grid[i+2][index+2],grid[i+1][index+1],grid[i][index]])
        repeat.add(sm)
        if len(repeat) > 1:
            return False
       
        
        return True
        
        
        
        
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        for i in range(row*col):
            rw = i//col
            cl = i%col
            if cl+3 <= col and rw+3<=row:
            
                if  self.distinct(rw,cl,grid):
                    if self.check(rw,cl,grid):
                        count+=1
                    

                        
        return count
        