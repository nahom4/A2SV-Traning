class Solution:
    
    def find(self,matrix,low,high,target):

            if (low > high):
                return False
   
     
     
            md = (low + high)//2
            row = md//len(matrix[0])
            col = md%len(matrix[0])
        
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = md+1
                return self.find(matrix,low,high,target)
             
            else:
                high = md-1
                return self.find(matrix,low,high,target)
        
    

    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        return self.find(matrix,0,len(matrix)*len(matrix[0])-1,target)
        
        
        
   
    
                    
            
                
        
        
        
        
        
        
    