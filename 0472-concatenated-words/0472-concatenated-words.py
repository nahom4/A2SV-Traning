class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        
        def  numWords(word):
            N = len(word)
            cache = {N : 0}
            def dp(i):
                if i in cache:
                    return cache[i]
                
                count = 0
                for j in range(i, N):
                    sub = word[i : j + 1]
                    if sub in dictionary:
                        prevCount = dp(j + 1)
                        
                        if prevCount == 0 and j != N - 1:
                            continue
                        
                        count = max(count ,prevCount + 1)
                    
                cache[i] = count
                return count
            
            return dp(0)
                            
        ans = []
        for word in words:
            if numWords(word) > 1:
                ans.append(word)
                
        return ans