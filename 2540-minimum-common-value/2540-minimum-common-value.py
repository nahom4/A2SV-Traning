class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums2= set(nums2)
        
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
            
        return -1
        