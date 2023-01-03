import numpy
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
            #check if each row is equal with each col


            count = 0
                
            hashed_row = [hash(tuple(n)) for n in grid]
                    
  
            grid = numpy.transpose(grid)
            hashed_col = [hash(tuple(m)) for m in grid]
        
            for row in hashed_row:
                for col in hashed_col:
                    
                    if row == col:
                        count+=1
            return count
                        
                        
                    
                    
                