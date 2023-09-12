class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        countCounter = Counter()
        for key in count:
            countCounter[count[key]] += 1
             
        letters = set(s)
        ans = 0
    
        for letter in letters:
            letterCount = count[letter]
            countCount = countCounter[letterCount]
            
            if countCount <= 1:
                continue
               
            countCounter[letterCount] -= 1
            while countCount >= 1:
                
                letterCount -= 1
                ans += 1
                countCount = countCounter[letterCount]
                
            if letterCount > 0:
                countCounter[letterCount] += 1
                
            
        return ans
                
                
                
            
                
                
            
            
        