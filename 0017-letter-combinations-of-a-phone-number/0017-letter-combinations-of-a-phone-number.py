class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letterReference = {"2" : ["a","b","c"],"3":["d","e","f"],"4" : ["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9" : ["w","x","y","z"]}
        answer = set()
        lis = []
        def backtrack(index):
                
            if index >= len(digits):
                if lis:
                    answer.add("".join(lis))
                return
            
            for letter in letterReference[digits[index]]:
                lis.append(letter)
                backtrack(index + 1)
                lis.pop()
                
        backtrack(0)
        
        return answer
            
            