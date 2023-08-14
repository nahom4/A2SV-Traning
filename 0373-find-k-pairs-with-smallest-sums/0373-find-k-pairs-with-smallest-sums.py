class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heapify(heap)
        
        for num in nums1:
            sm = num + nums2[0]
            pair = (num,nums2[0])
            index = 1
            heapq.heappush(heap,(sm,pair,index))
           
        ans = []
        while heap:
            sm,pair,index = heapq.heappop(heap)
            ans.append(pair)
            if index < len(nums2):
                nextValue = nums2[index]
                base = pair[0]
                sm = base + nextValue
                index += 1
                pair = (base,nextValue)
                heapq.heappush(heap,(sm,pair,index))
            
            if len(ans) == k:
                break
                
        return ans
            
        
                
        