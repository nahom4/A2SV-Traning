class Solution:
    pairs = 0
    def reversePairs(self, nums: List[int]) -> int:
        
        def calculate(left_side,right_side):
            first = 0
            second = 0
            while first < len(left_side) and second < len(right_side):
                if left_side[first] > right_side[second] * 2:
                    self.pairs += len(left_side) - first
                    second += 1
                else:
                    first += 1
         
            
        def merge_sort(left,right):
            if left >= right:
                return [nums[left]]
            md = left + (right - left) // 2
            left_side = merge_sort(left,md)
            right_side = merge_sort(md + 1,right)
            
            return merge(left_side,right_side)
        
        
        
        def merge(left_side,right_side):
            
            first = 0
            second = 0
            result = []
            calculate(left_side,right_side)
            while first < len(left_side) and second < len(right_side):
                
                if left_side[first] <= right_side[second]:
                    
                    result.append(left_side[first])
                    first += 1
                    start = True
                else:
                    result.append(right_side[second])
                    second += 1
                    
                    
                  
            result.extend(left_side[first:])
            result.extend(right_side[second:])
            
            return result
        
        merge_sort(0,len(nums) - 1)
        return self.pairs
                    
                
            
            
    
            
        