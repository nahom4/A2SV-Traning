from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        size = len(nums)
        
        for x in count:
            if count[x] > size//2:
                return x
        
                
        