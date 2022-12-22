class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for index in range(1,len(strs)):
            i = 0
            temp = ''
            while i < len(prefix) and i<len(strs[index]):
                #compare prefix and the words in strs
                
                
                if prefix[i] == strs[index][i]:
                    temp+=prefix[i]
                    
                else:
                    break
                    
                i+=1
                    
        
            prefix = temp
            
        
            
            
        return prefix