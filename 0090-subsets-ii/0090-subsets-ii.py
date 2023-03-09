class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        ans = []
        nums.sort()
        #the problem is finding combinations of size k
        
        
        def comb(index,k):
            
            if len(ans) == k:
                new = tuple(ans)
                if not new in result:
                    result.add(new)
                    return
            
            if index >= len(nums):
                return
            
            comb(index + 1,k)
            ans.append(nums[index])
            comb(index + 1,k)
            ans.pop()
            
        for i in range(0,len(nums) + 1):
            comb(0,i)
        
        result = [list(val) for val in result]
        return result