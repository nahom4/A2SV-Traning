

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        dic = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dic[i-j].append(matrix[i][j]) 
                if dic[i-j][0] != matrix[i][j]:
                    return False
                
        return True
        
  
        