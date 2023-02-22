class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        n = len(s2)
        
        count_s1 = [0]*26
        count_s2 = [0]*26
        
        left = 0
        
        for letter in s1:
            count_s1[ord(letter)- ord('a')] += 1
            
        for right in range(n):
            
            #add
            count_s2[ord(s2[right]) - ord('a')] += 1
            
            #validate
            
            if right - left + 1 == k:
                
                if count_s2 == count_s1:
                    return True
                
                #remove 
                count_s2[ord(s2[left]) - ord('a')] -= 1
                left += 1
                
        return False
        
       
        
        
        