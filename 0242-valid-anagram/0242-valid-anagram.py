from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first = Counter(s)
        second = Counter(t)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if first.get(s[i],0) == second.get(s[i],0):
                continue
            else:
                return False
        return True