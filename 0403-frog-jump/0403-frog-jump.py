class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        start = stones[0]
        secondStone = stones[1]
        stones = set(stones)
        cache = {}
        def backTrack(stone,k):
            
            if not stone in stones:
                return False
            
            if stone == target:
                return True
            
            if k == 0:
                return False
            #moves k - 1, k , k + 1
            
            if (stone,k) in cache:
                return cache[(stone,k)]
            
            first,second,third = k - 1,k, k + 1
            firstStone,secondStone,thirdStone = stone + first,stone + second,stone + third
            
            isFirstValid = backTrack(firstStone,first)
                
            isSecondValid = backTrack(secondStone,second)
                
            isThirdValid = backTrack(thirdStone,third)
                
            cache[(stone,k)] = isFirstValid or isSecondValid or isThirdValid
            
            return cache[(stone,k)]
        
        if start + 1 < secondStone:
            return False
        
        return backTrack(secondStone,1)