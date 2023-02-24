class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        #The trick use remainders
        
        size = len(nums)
        dic = defaultdict(int)
        total = 0
        
        for i in range(size):
            
            total += nums[i]
            dic[total%k] += 1
        result = 0  
       
        for key in dic:
            if key == 0:
                result += dic[key]
            result += (dic[key])*(dic[key] - 1)//2
        return result
                
            
        
        
        