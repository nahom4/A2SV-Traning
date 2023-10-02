class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
         of the top the approach I would use is to 
         count the size of the contigious A's and B's
        """
        i = 1
        ans = {"A": 0, "B" : 0}
        currCount = 1
        colors += "*"
        colors = "*" + colors
        N = len(colors)
        while i < N - 1:
            letter = colors[i]
            if letter == colors[i + 1]:
                currCount += 1
                
            else:
                if currCount >= 3:
                    ans[letter] += currCount - 2
                    
                currCount = 1
           
            i += 1
            
        if ans["A"] <= ans["B"]:
            return False
        else:
            return True

                
                
            
                
            
        
        