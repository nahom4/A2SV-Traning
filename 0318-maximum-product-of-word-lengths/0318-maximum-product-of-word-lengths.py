class Solution:
    def maxProduct(self, words: List[str]) -> int:
        num = 0
        mx_length = 0
        new = []
        for i, word in enumerate(words):
            num = 0
            for letter in word:
                num = num | (2 ** (ord(letter) - 97))
            new.append(num)
        for i in range(len(new)):
            for j in range(i,len(new)):
                if new[i] & new[j] == 0:
                    mx_length = max(mx_length,(len(words[j]) * len(words[i])))
        return mx_length
                    
            
        