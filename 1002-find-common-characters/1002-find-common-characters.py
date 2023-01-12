class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        
        for latter in ascii_lowercase:
            count = float("inf")
            for word in words:
                if word.count(latter) <= count:
                    count = word.count(latter)
            for _ in range(count):
                ans.append(latter)
                
        return ans
                
        
                
   
                    
     
                
                
        