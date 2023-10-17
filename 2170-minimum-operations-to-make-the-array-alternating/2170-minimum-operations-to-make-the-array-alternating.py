class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        even = Counter()
        odd = Counter()
        N = len(nums)
        for i in range(N):
            if i % 2:
                odd[nums[i]] += 1
                
            else:
                even[nums[i]] += 1

        even = sorted(list(even.items()),reverse = True,key = lambda x : x[1])
        odd = sorted(list(odd.items()),reverse=True,key = lambda x : x[1])
        even.append((-1,0))
        odd.append((-1,0))
        
        even,odd = even[: 2],odd[: 2]
        
        N = len(nums)
        if even[0][0] != odd[0][0]:
            return N - even[0][1] - odd[0][1]
        else:
            return min(( N - even[0][1] - odd[1][1]),(N - odd[0][1] - even[1][1]))
           
      
            
        
        