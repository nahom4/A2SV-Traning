class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        
        count = 0
        for x in range(len(words)):
            for i in range(x+1,len(words)):
                if set(words[x]) == set(words[i]):
                    count+=1
                    
                    
        return count
                    
                
        