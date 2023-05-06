class KthLargest:

    def __init__(self, k: int, nums: List[int]):
     
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
        if self.k < len(self.nums ):
            for _ in range(len(self.nums) - k):
                heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
       
        if not self.nums:
            heapq.heappush(self.nums,val)
            return val
            
        if self.nums and val >= self.nums[0]:
            heapq.heappush(self.nums,val)
            
        else:
            if len(self.nums) < self.k:
                heapq.heappush(self.nums,val)
                
            
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]
            
            
            
            
       
    
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)