class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ct = 0
        for i in range(N):
            curr = nums[i]
            tg = target - curr
            rightBound = bisect.bisect_right(nums,tg)
            if rightBound > i:
                ct += 2 ** (rightBound - i - 1)
            
        return ct %  (10 ** 9 + 7)