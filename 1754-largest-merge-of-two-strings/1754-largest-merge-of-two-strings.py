class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        lis = []
        
        while i<len(word1) and j<len(word2):
            if word1[i] < word2[j]:
                lis.append(word2[j])
                j+=1
            elif word1[i] == word2[j] :
                
                if word1[i:] > word2[j:]:
                    lis.append(word1[i])
                    i+=1
                else:
                    lis.append(word2[j])
                    j+=1
            
                
                
                
          
                
            else:
                lis.append(word1[i])
                i+=1
                
        while i<len(word1):
                lis.append(word1[i])
                i+=1
                
        while j < len(word2):
                 lis.append(word2[j])
                 j+=1
        return ''.join(lis)
            
                
            
                
                
        