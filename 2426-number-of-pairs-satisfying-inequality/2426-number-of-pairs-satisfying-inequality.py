class Solution:
    pairs = 0
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
            
        nums = nums1
            
        
        def calculate(left_side,right_side,diff):
            first = 0
            second = 0
            while first < len(left_side) and second < len(right_side):
                if left_side[first] <= right_side[second] + diff:
                    self.pairs += len(right_side) - second
                    first += 1
                else:
                    second += 1
         

        def merge(left_side,right_side,diff):
            
            calculate(left_side,right_side,diff)
            
            first = 0
            second = 0
            result = []
          
            while first < len(left_side) and second < len(right_side):
                
                if left_side[first] <= right_side[second]:
                    result.append(left_side[first])
                    first += 1
                else:
                    result.append(right_side[second])
                    second += 1
                    
            result.extend(left_side[first:])
            result.extend(right_side[second:])
            return result
                    
                    
        
        def merge_sort(left,right):
            
            if left >= right:
                return [nums[left]]
            
            md = left + (right - left) // 2
            
            left_side = merge_sort(left,md)
            right_side = merge_sort(md + 1,right)
            
            return merge(left_side,right_side,diff)
        
        merge_sort(0,len(nums) - 1)
        return self.pairs
        
        