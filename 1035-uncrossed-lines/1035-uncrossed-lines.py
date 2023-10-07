class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i,j):
            #we will work on nums1 
            N = len(nums1)
            M = len(nums2)
            
            if i >= N or j >= M:
                return 0
            
            
            for index in range(j,M):
                if nums2[index] == nums1[i]:
                    break
                   
            
            leave = dp(i + 1,j)
            take = 0
            if nums2[index] == nums1[i]:
                take  = dp(i + 1,index + 1) + 1
                
            return max(take,leave)
        
        return dp(0,0)