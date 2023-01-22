class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        location = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    location.append([i,j])
                    
        for loc in location:
            for i in range(len(matrix[0])):
                matrix[loc[0]][i] = 0
            for j in range(len(matrix)):
                matrix[j][loc[1]] = 0
        
            
        