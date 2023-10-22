class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        """
            calculate min values going to the right and to left of k
        """
        N = len(nums)
        cache = [0] * N
        cache[k] = nums[k]
        for i in range(k + 1,N):
            cache[i] = min(cache[i - 1],nums[i])
            
        for i in range(k - 1,-1,-1):
            cache[i] = min(cache[i + 1],nums[i])
            
        #place the right pointer as far as possible
        left = k
        right = k
        mn = float("inf")
        ans = nums[k]
        currSize = 0
        while left > 0 or right < N - 1:
            currSm = cache[right] * (right - left + 1)
            moveLeft = (min(mn,cache[left - 1]) * (right - left + 2)) if left > 0 else 0
            moveRight = min(mn,cache[right + 1]) * (right - left + 2) if right < N - 1 else 0
            if moveLeft  > moveRight:
                left -= 1 
            else: 
                right += 1
           
            mn = min(mn,cache[left] if left >= 0 else float("inf"),cache[right] if right < N else float("inf"))
            ans = max(ans,moveLeft,moveRight)
            
        return ans
                
                    
                
      
        
            
            
        
            
        