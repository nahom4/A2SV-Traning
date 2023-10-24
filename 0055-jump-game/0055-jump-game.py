class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #a player is only in trouble if he reaches a position
        #that is 0 if it is able to pass all this points then it is good
        #I need to hold max forward jump
        
        forward  =  0
        N = len(nums)
        for i in range(N):
            forward -= 1
            forward = max(forward,nums[i])
            if i == N - 1:
                return True
            if forward <= 0:
                return False
            
        return True
        