class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        #the new matrix 
        new = [['' for _ in range(c)] for _ in range(r)]
        print(new)
        
        index = 0
        
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
             
                row = index//c
                col = index%c
                if row < r and col < c:
                    new[row][col] = mat[i][j]
                else:
                    return mat
                index+=1
                
        for row in range(r):
            for col in range(c):
                if new[row][col] == '':
                    return mat
                
            
        
        return new
       
                
        