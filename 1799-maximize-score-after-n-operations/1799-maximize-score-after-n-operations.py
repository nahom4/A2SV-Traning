class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
            
        cache = {}
        #let's do it brute force  p
        def backTrack(nums,opp):
            nums.sort()
            test = tuple(nums)
            if test in cache:
                return cache[test]
            currMax = 0
            N = len(nums)
            for i in range(N):
                for j in range(i + 1,N):
                    newList = list(nums)
                    newList.pop(i)
                    newList.pop(j - 1)
                    currScore = opp * gcd(nums[i],nums[j])
                    res = backTrack(newList,opp + 1)
                    currMax = max(res + currScore,currMax)
                    
            nums.sort()
            cache[tuple(nums)] = currMax
            return currMax
        
        return backTrack(nums,1)
                    
                
                
            