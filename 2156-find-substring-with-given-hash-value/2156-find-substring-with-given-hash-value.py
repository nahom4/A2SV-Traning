class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        N = len(s)
        currHash = 0
        left = 0
        s = s[:: - 1]
        pw = power ** (k - 1)
        ans = None
        for i in range(N):
            #add
            idx = ord(s[i]) - ord("a") + 1
            currHash *= (power % modulo)
            currHash += idx
            currHash %= modulo
          
            if i - left + 1 == k:
               
                if currHash  == hashValue:
                    ans = s[left : i + 1]

                idx = ord(s[left]) - ord("a") + 1
                currHash -= (idx * pw)
                currHash %= modulo
                left += 1
                
        return ans[:: -1]
                
           
                
                
       

            
            