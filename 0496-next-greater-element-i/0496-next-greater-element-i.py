
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dic= defaultdict()
        mono_stack = []
        #we add to a stack 
        for i in range(len(nums2) - 1, -1,-1):
            
            if len(mono_stack) == 0:
                mono_stack.append(nums2[i])
                dic[nums2[i]] = -1
            else:
                
                while len(mono_stack) > 0 and mono_stack[-1] < nums2[i]:
                    
                    mono_stack.pop()
                if len(mono_stack) > 0:
                    dic[nums2[i]] = mono_stack[-1]
                    
                else:
                    dic[nums2[i]] = -1
                    
                mono_stack.append(nums2[i])
            
        for i in range(len(nums1)):
            nums1[i] = dic[nums1[i]]
            
        return nums1