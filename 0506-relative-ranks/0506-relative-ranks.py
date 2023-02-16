class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        
        new = []
        for x in score:
            new.append(x)
        
        new.sort(reverse=True)
        comp = dict()
        for i in range(len(new)):
            comp[new[i]] = i
        
        for i in range(len(score)):
            if comp[score[i]] == 0:
                score[i] ="Gold Medal"
                continue
            if comp[score[i]] == 1:
                score[i]= "Silver Medal"
                continue
            if comp[score[i]] ==  2:
                score[i] = "Bronze Medal"
                continue
            else:
                score[i] = str(comp[score[i]]+1)
                continue
        return score
        
        