from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        count  = Counter(nums2)
        
        for i in range(len(nums1)):
          
            if count.get(nums1[i],0) != 0:
                
                result.append(nums1[i])
                count[nums1[i]]-=1
               
                
        return result
                
        
        