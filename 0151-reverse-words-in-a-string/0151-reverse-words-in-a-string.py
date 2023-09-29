class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split(" ")
        ans = ans[:: - 1]
        newAns = []
        for word in ans:
            if word != "":
                newAns.append(word)
                
        return " ".join(newAns)
        