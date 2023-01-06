class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        #Track the elements using a dictianry
        
        position = {}
        
        for i, x in enumerate(nums):
            position[x] = i
            
        for first,second in operations:
            
            pos = position[first]
            
            nums[pos] = second
            position[second]= pos
            del(position[first])
        return nums
            
            
            
            
        
    
                    
                
                
                
                
                
            
        