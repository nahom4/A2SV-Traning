class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sortedPairs = sorted(pairs,key=lambda k : k[1])
        chain = [sortedPairs[0]]
        N = len(sortedPairs)
        for i in range(1,N):
            if chain[-1][1] < sortedPairs[i][0]:
                chain.append(sortedPairs[i])
                   
        return len(chain)
           
            
