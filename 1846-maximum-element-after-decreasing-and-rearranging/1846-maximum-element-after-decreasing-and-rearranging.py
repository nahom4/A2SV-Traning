class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        ans = [1]
        
        for index in range(1,len(arr)):
       
            if ans[-1] < arr[index]:
                ans.append(ans[-1] + 1)
                
        return ans[-1]
            
            
        