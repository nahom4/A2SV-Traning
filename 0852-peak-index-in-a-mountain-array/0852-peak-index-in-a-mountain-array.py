class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        low = -1 
        high = len(arr)
        
        while high > low + 1:
            md = low + (high - low)//2
            
            if md + 1 < len(arr) and arr[md] > arr[md + 1]:
                             
                high = md
            else:
                low = md
                
        return high
                
        
                             
                             
                            
                             
                            