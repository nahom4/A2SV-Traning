class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        #let's use prefix sum to solve the problem
        size = 1002
        array = [0]*size
        
        for trip in trips:
            
            cap,start,end = trip
            array[start] += cap
            array[end] -= cap
        
        #do prfix sum
        for i in range(size):
            array[i] += array[i - 1]
            
     
        #go through the sum to look for spots where cap is greater than capacity
        flag = True
        for i in range(size):
            
            if capacity < array[i]:
                flag = False
                
        return flag
            
            
            
        