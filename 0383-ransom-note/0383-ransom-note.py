from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = Counter(magazine)
        
        for x in ransomNote:
            if count.get(x,0) == 0:
                return False
            else:
                count[x] -=1
        return True
        