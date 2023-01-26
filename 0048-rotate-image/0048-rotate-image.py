class Solution:
    
    def swap(self,i,j,matrix,temp):
        
      
       
        n = len(matrix[0])-1
        
        
        value = matrix[j][n-i]
        matrix[j][n-i] = temp
        return [(j,n-i),value]
    def rotate(self, matrix: List[List[int]]) -> None:
     
        
       
        checked = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not (i,j) in checked:
                    
                   
                    temp = matrix[i][j]
                    first = i
                    second = j
                 
                    for _ in range(4):
                        nxt = self.swap(first,second,matrix,temp)
                        checked.add((first,second))
                        first,second = nxt[0]
                        temp = nxt[1]
                        
                  
                   
                   
               
                
            
        