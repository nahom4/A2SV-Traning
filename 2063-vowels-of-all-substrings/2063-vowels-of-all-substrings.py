class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = set(["a","e","i","o","u"])
        sm = 0
        N = len(word)
        
        for i in range(N):
            if word[i] in vowels:
                sm += (i + 1) * (N - i)
                
        return sm
        