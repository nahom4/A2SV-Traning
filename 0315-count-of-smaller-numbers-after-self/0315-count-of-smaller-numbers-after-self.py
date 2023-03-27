class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        final = [0] * len(nums)
        dic = dict()
        for i in range(len(nums)):
            nums[i] = [nums[i],i]
        
        def count_less(left_side,right_side,left):
            
            first = 0
            second = 0
            count = 0
            
            
            while first < len(left_side) and second < len(right_side):
                
                if left_side[first][0] > right_side[second][0]:
                    count += 1
                    second += 1
                else:
                    final[left_side[first][1]] += count
                    first += 1
            while first < len(left_side):
               
                final[left_side[first][1]] += count
                first += 1
                    
            
            
            
        
        def merge(left_side,right_side,left):
            
            count_less(left_side,right_side,left)
            
            first = 0
            second = 0
            result = []
          
            while first < len(left_side) and second < len(right_side):
                
                if left_side[first][0] <= right_side[second][0]:
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
            
            return merge(left_side,right_side,left)
        
        merge_sort(0,len(nums) - 1)
        return final
        