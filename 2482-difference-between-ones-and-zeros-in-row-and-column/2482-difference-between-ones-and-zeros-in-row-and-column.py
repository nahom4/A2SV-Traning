class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        #lets prepare four lists to hold number of 0s and 1 in col and rows
        
        new = [["" for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        row1 =[]
        row0 = []
        
        col0 = []
        col1 = []
   
        
        for row in range(len(grid)):
            zero = 0
            one = 0
            for col in range(len(grid[0])):
                
                if grid[row][col] == 0:
                    zero += 1
                else:
                    one+=1
                    
            row1.append(one)
            row0.append(zero)
                    
    
        for col in range(len(grid[0])):
            zero = 0
            one = 0
            for row in range(len(grid)):
                
                if grid[row][col] == 0:
                    zero += 1
                else:
                    one+=1
                    
            col1.append(one)
            col0.append(zero)
            
   
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                total = 0
                total = row1[x] + col1[y] - row0[x] - col0[y]
                
                new[x][y] =total
                
        return new
                
                
                
                
        