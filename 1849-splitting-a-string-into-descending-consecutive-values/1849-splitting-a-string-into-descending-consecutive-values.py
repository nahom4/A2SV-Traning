class Solution:
    def splitString(self, s: str) -> bool:
        lst = []
        self.ans = False
        size = len(s)
        def split_string(s,lst,ans):
            
            if len(lst) >= 2:
                if int(lst[-2]) <= int(lst[-1]) or int(lst[-2]) - int(lst[-1]) != 1 :
                    lst.pop()
                    return
            if  len(lst) > 1 and len(''.join(lst)) == size:
                
                self.ans = True
                return
                
            for i in range(len(s)):
                
                lst.append(s[:i + 1])
                
                if i < len(s):
                    split_string(s[i + 1:],lst,ans)
                    
            if lst:
                lst.pop()
            
        split_string(s,lst,self.ans)
        return self.ans
                
            
                
                
            
        
        
        