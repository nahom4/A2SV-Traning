class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        #binary search function
        def binary_search(value):
            low = -1
            high = len(words) 
            
            while high > low + 1:
                
                md  = low + (high - low)//2
                if words[md] > value:
                    high = md
                else:
                    low = md
            
            return len(words) - high 
        #count the least letter
        def count_lower(s):
            s = list(s)
            s.sort()
            return s.count(s[0])
        
        #lets preprocess queris
        for i in range(len(queries)):
            
            queries[i] = count_lower(queries[i])
            
        
            
        #lets preprocess words
        for i in range(len(words)):
            
            words[i] = count_lower(words[i])
          
        words.sort()
        
        #now let's do binary search on queries
    
        for i in range(len(queries)):
            
            queries[i] = binary_search(queries[i])
            
        return queries
            
        
            
        