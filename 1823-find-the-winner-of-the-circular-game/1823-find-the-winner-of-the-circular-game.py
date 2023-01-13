class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle =  [i for i in range(1,n+1)]
        
        start = 0
        
        while len(circle)>1:
            
            target = (start+k-1)%len(circle)
            circle.pop(target)
            start = target
        return circle[0]
            