class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            the even odd cases
            the array that doesn't finish correctly
        """
        
        
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2,nums1
        
        left,right = 0,len(nums1) - 1
        while True:
        
            md = (left + right) // 2
            j = (half - md) - 2
            leftA = nums1[md] if md >= 0 else float("-inf")
            rightA = nums1[md + 1] if (md + 1) < len(nums1) else float("inf")
            leftB = nums2[j] if j >= 0 else float("-inf")
            rightB = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")
            

            if leftA <= rightB and leftB <= rightA:# the partion works
                
                if total % 2:
                    return min(rightA,rightB)
                else:
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2
                
            
            if leftA < rightB:
                left = md + 1
                
            else:
                right = md - 1
                
        
        