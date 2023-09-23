class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPredecessor(A,B):
            
            if not (len(B) == len(A) + 1):
                return False
            
            bumbs = 0
            pointerA = 0
            pointerB = 0
            
            while pointerA < len(A) and pointerB < len(B):
                
                if A[pointerA] != B[pointerB]:
                    bumbs += 1
                    pointerB += 1
                    
                else:
                    pointerA += 1
                    pointerB += 1
                
            if bumbs <= 1:
                return True
            else:
                return False
            
        words = sorted(words,key= lambda word : len(word))
        cache = {}
        finalAns = 1
        N = len(words)
        for i in range(N):
            maxLength = 0
            for j in range(i):
                if isPredecessor(words[j],words[i]):
                    maxLength = max(maxLength,cache[j])
                    
            cache[i] = maxLength + 1
            finalAns = max(finalAns,cache[i])
            
        
        return finalAns
                    
            
                
        