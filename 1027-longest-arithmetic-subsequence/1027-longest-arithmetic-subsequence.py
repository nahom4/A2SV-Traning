class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
       
        maxDiff = max(nums) - min(nums)
        cache = {}
        N = len(nums)
        for i in range(N):
            currValue = nums[i]
            tempDic = dict()
            
            for diff in range(-(maxDiff),maxDiff + 1):
                prevValue = currValue - diff
                prevCount = 0
                if prevValue in cache:
                    prevCount = cache[prevValue][diff]
                
                tempDic[diff] = prevCount + 1
            cache[currValue] = tempDic
            
        maxLength = float("-inf")
        for key in cache:
            for value in cache[key]:
                maxLength = max(maxLength,cache[key][value])

        return maxLength

                


        