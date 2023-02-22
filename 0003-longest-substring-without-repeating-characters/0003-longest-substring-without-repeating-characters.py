class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique = set()
        left = 0
        max_length = 0
        
        for right in range(n):
            
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length
            
        
                
        