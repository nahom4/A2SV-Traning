class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        #for three numbers to be the sides of a triangele the sum
        #of the two smallest need to be smaller than the largest
        #number
        
        #first let's sort and then check every three set of elements if they can form a triangle
        nums.sort(reverse=True)
    
        
        i = 0
        
        while i < len(nums)-2:
            if nums[i] < nums[i+1] +nums[i+2]:
                return nums[i] +nums[i+1] + nums[i+2]
           
                
            i+=1
        return 0
                
            
        