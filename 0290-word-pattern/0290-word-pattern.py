class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        dic = dict()
        
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        for i, x in enumerate(pattern):
            
            if dic.get(x,0) == 0 or dic.get(x) == s[i]:
            
                dic[x] = s[i]
            else:
                return False
        
    
        new_dic = dict()
        
        
            
        for i, x in enumerate(s):
            
            if new_dic.get(x,0) == 0 or new_dic.get(x) == pattern[i]:
            
                new_dic[x] = pattern[i]
            else:
                return False
        
        
        return True
            