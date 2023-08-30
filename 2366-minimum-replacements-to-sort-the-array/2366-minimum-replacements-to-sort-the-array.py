class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        minElement = nums[-1]
        N = len(nums)
        count = 0
        for i in range(N - 1,-1,-1):
            currentElement = nums[i]
            if nums[i] > minElement:
                currentCount = currentElement // minElement
                remainder = nums[i] % minElement
                if remainder == 0:
                    currentCount -= 1
                minElement = currentElement // (currentCount + 1)   
                count += currentCount
            else:
                minElement = currentElement
                         
        return count