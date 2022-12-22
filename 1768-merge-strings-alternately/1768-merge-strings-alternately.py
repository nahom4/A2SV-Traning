class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j =0
        on = True
        result = ''
        while i<len(word1) and j < len(word2):
            
            if on:
                result += word1[i]
                i+=1
                on = False
            else:
                result += word2[j]
                j+=1
                on = True
                
        while i < len(word1):
            result+= word1[i]
            i+=1
        while j< len(word2):
            result += word2[j]
            j+=1
            
        return result

                            
            
            
        