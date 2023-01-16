class Solution:

    def three(self,row_start,row_end,col_start,col_end,grid):
       
        total = 0
        for rw in range(row_start, row_end+1):
            for cl in range(col_start, col_end+1):
                total = max(total,grid[rw][cl])
                
        return total

        
        
        
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_start = 0
        row_end = 2
        col_start = 0
        col_end = 2

        grid_end  = len(grid[0])-1
        grid_row_end = len(grid)-1

        result = 0
        lis = []

        while row_end <= grid_row_end:
            temp = []
            while col_end <= grid_end:
               
                result =  self.three(row_start,row_end,col_start,col_end,grid)
                temp.append(result)
                col_end+=1
                col_start+=1
            lis.append(temp)

            row_start+=1
            row_end+=1
            col_start = 0
            col_end = 2
            
          
        return lis
        