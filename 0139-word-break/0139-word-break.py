class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        wordDict = set(wordDict)
        cache = {N : True}
        def backTracking(i):
            
            if i in cache:
                return cache[i]
           
            isValid = False
            for j in range(i, N):
                
                sub = s[i : j + 1]
                if sub in wordDict:
                    isValid = isValid or backTracking(j + 1)
                    
            cache[i] = isValid
            return isValid
        
        return backTracking(0)