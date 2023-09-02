class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        wordDict = set(wordDict)
        cache = {N : [[]]}
        def dp(i):
            
            if i in cache:
                return cache[i]
            
            subList = []
            for j in range(i,N):
                sub = s[i : j + 1]
                if sub in wordDict:
                    lis = dp(j + 1)
    
                    for value in lis:
                        subList.append([sub] + value)
                        
            cache[i] = subList
            return cache[i]
        ans = dp(0)
        for i in range(len(ans)):
            ans[i] = " ".join(ans[i])
            
        return ans
        