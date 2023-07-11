class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num1 = num2 = float('inf')
        
        for num in nums:
            if num > num2:
                return True
            
            if num > num1:
                num2 = min(num,num2)
                
            num1 = min(num1, num)
            
        