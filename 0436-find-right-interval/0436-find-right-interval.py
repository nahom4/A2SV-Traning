class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        #we will search over the start  part of the interval since the start is unique and
        #we can put in a dictionary
        memory = dict()
        start = []
        result_list = [-1]*len(intervals)
        for i, interval in enumerate(intervals):
            memory[interval[0]] = i
            start.append(interval[0])
        
        #sort start
       
        start.sort()
      
        def binary(value):
            
            low = -1
            high = len(start)
            
            while high > low + 1:
                
                md = low + (high - low) // 2
                
                if start[md] >= value:
                    high = md
                else:
                    low = md
               
            return high
        
        for i in range(len(intervals)):
            
            result = binary(intervals[i][1])
            
            if result == len(start):
                pass
            else:
                result_list[i] = memory[start[result]]
        return result_list
            
        
            
        
        