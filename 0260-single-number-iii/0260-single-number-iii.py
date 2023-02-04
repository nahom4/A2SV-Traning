from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        ans = []
        for x in count:
            
            if count[x] == 1:
                ans.append(x)
                
        return ans
            
        