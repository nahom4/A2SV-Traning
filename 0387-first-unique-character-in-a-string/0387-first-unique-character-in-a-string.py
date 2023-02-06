from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(s)
        
        for i, x in enumerate(s):
            if count[x] == 1:
                return i
            
        return -1
        