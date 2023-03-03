class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity):
            total_days = 0
            running_sum = 0
            for i in range(len(weights)):
                
                running_sum += weights[i]
                
                if i == len(weights) - 1:
                    total_days += 1
                    if running_sum > capacity:
                        total_days += 1
                
                elif running_sum == capacity:
                    total_days += 1
                    running_sum = 0
                
                elif running_sum > capacity:
                    total_days += 1
                    running_sum = weights[i]
            return total_days
        
        #The binary search space is max(weights) and sum(weights)
        
        low = max(weights) - 1  
        high = sum(weights) + 1
        
        while high > low + 1:
            md = low + (high - low)//2
            
            if check(md) <= days:
                
                high = md
            else:
                low = md
                
        return high
                    
            
            
                    
                
                    
                    
                
                
                