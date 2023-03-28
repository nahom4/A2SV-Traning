class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        result = []
        
        def backtrack(left):
            
            if len(res) > 4:
                return
            if len(res) == 4 and left >= len(s):
                result.append('.'.join(res))
                return
            
            if left >= len(s):
                return
            
            for index in range(left,len(s)):
               
                value = s[left:index + 1]
                if len(value) > 1 and value[0] == '0':
                    continue
                if int(value) <= 255:
                    res.append(value)
                    backtrack(index + 1)
                    res.pop()
                
                
        backtrack(0)
        return result
                
            
        