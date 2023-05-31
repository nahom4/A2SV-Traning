class Solution:
    def tribonacci(self, n: int) -> int:
        
        array = [0] * (n + 1)
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        array[0],array[1],array[2] = 0,1,1        
        for i in range(3,n + 1):
            array[i] = array[i - 1] + array[i - 2] + array[i - 3]
            
        return array[-1]
            
       

       
            
        
        
        
        