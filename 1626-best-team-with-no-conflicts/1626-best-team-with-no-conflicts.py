class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        """
            let's try an n^2 solution where at each point we back ward and calcul
            ate a new sum and at the end return max sum 
        """

        finalAns =  float("-inf")
        N = len(scores)
        cache = [0] * (N)
        
        newList = []
        for i in range(N):
            newList.append((ages[i],scores[i]))
             
        newList.sort(reverse=True)
        scores = []
        for i in range(N):
            scores.append(newList[i][1])
        
        for i in range(N):
            currSum = scores[i]
            score = 0
            for j in range(i - 1,-1,-1):
                currScore = scores[j]
                if currScore < scores[i]:
                    continue
                
                score = max(score,cache[j])

            cache[i] = score + currSum
            finalAns = max(finalAns,cache[i])
        return finalAns