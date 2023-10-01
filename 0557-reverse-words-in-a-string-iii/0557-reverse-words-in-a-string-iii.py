class Solution:
    def reverseWords(self, s: str) -> str:
        sp  = s.split()
        N = len(sp)
        for i in range(N):
            sp[i] = sp[i][:: -1]
            
        return " ".join(sp)
        