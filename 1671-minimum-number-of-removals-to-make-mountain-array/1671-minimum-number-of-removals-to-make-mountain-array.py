class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        def monotonSeq(nums):
            N = len(nums)
            cache = [1] * N

            for i in range(N):
                mxLength = 0
                for j in range(i):
                    if nums[i] > nums[j]:
                        mxLength = max(mxLength,cache[j])

                cache[i] = mxLength + 1

            return cache
        
        inc = monotonSeq(nums)
        dec = monotonSeq(nums[:: -1])[:: -1]
        N = len(inc)
        maxLength = 1
 
        for i in range(len(inc)):
            if inc[i] == 1 or dec[i] == 1:
                continue
            maxLength = max(maxLength,inc[i] + dec[i] - 1)
            
        return N - maxLength

        