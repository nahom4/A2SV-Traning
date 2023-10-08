class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #let's use a two pointer approach
        start = 0
        end = 0
        N = len(gas)
        totalGas = 0
        ct = 0
        while start < N: # 1,2,3,4,5  3,4,5,1,2 2
            
            totalGas += (gas[end] - cost[end]) 
            if ct == N and start == end:
                return start
            if totalGas >= 0:
                end += 1
                ct += 1
                
            else:
                if end < start:
                    return -1
                end += 1
                ct,start,totalGas = 0,end,0
                
            end = end % N
            
        return -1
            
            
            
            
            
        