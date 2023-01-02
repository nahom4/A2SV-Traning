class Solution:
    def check(self,s,t):
         #let's use a dictionary
        
        mapping = dict()
        
        for i in range(len(s)):
            temp = mapping.get(s[i],0)
            if temp == 0:
                mapping[s[i]] = t[i]
            else:
                if temp == t[i]:
                    continue
                else:
                    return False
        return True
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return self.check(s,t) and self.check(t,s)
       
        