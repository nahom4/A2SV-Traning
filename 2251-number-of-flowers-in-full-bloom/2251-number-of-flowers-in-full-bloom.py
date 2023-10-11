class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        startingTimes = []
        endingTimes = []
        
        N = len(flowers)
        for i in range(N):
            startingTimes.append(flowers[i][0])
            endingTimes.append(flowers[i][1])
            
        startingTimes.sort()
        endingTimes.sort()
          
        M = len(people)
        ans = []
        for i in range(M): 
            start = bisect.bisect_right(startingTimes,people[i])
            end = bisect.bisect_left(endingTimes,people[i])
            ans.append(start - end)
            
        return ans