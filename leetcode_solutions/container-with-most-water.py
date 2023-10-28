class Solution:
    def maxArea(self, height: List[int]) -> int:
        #let's use two pointers approach
        left =0
        right = len(height)-1
        mx= 0
        while left <right:
            area =  (right-left)*min(height[left],height[right])
            mx = max(area,mx)
            if height[left] > height[right]:
                right -= 1
            else:
                left+=1
           

        return mx

        
            

