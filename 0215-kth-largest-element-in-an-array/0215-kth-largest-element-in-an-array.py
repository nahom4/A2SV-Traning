class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick sort
        def quick_sort(left,right):
           
            if left > right:
                return
            read = left + 1
            write = left + 1
            pivot = nums[left]
            
            for read in range(left,right + 1):
                
                if nums[read] < pivot:
                    nums[read],nums[write] = nums[write],nums[read]
                    write += 1
            nums[left],nums[write - 1] = nums[write - 1],nums[left]
            if (len(nums) - (write - 1)) == k:
                return pivot
            
            elif (len(nums) - (write - 1)) > k:
                return quick_sort(write,right)
            else:
                return quick_sort(left,write - 2)
       
        return quick_sort(0,len(nums) - 1)
        
                
                
                
            
            
        
        