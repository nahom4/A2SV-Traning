class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        cache = {N : 0}
        dictionary = set(dictionary)
        def backTrack(start):
            
            if start in cache:
                return cache[start]
            value = 1 + backTrack(start + 1)
            for i in range(start,N):
                sub = s[start : i + 1]
                if sub in dictionary:
                    value = min(backTrack(i + 1),value)
                
            cache[start] = value
            return cache[start]
           
        return backTrack(0)
        