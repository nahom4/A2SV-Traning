class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        row = len(matrix)
        col = len(matrix[0])
        
        self.prefix_sum  = [[0]*( col + 1 ) for _ in range(row + 1)]
        
        #let's calcultate the prefix sum 
        
        for r in range(row):
            for c in range(col):
                self.prefix_sum[r+1][c+1] = self.prefix_sum[r+1][c] +  self.prefix_sum[r][c+1] + matrix[r][c] - self.prefix_sum[r][c]
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result = self.prefix_sum[row2 + 1][col2 + 1]
        left = self.prefix_sum[row2 + 1][col1]
        top = self.prefix_sum[row1][col2 + 1]
        difference = self.prefix_sum[row1][col1]
      
        return result - left - top + difference


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)