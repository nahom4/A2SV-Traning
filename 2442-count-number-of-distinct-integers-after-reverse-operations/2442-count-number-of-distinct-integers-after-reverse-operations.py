class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            temp = str(nums[i])
            new = temp[::-1]
            new = int(new)
            nums.append(new)
            
        st = set()
        
        for i in range(len(nums)):
            st.add(nums[i])
            
        return len(st)
        
        
        