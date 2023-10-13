class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        #bottom dp
        #each index will have to dictionaries increasing a decreasing
        
        N = len(rating)
        cache = [[0,0] for _ in range(N)]
        
        total = 0
        for i in range(N):
            num = rating[i]
            for j in range(i + 1):
                #for each j go over the increasing and decreasing
                currNum = rating[j]
                if currNum < num: # increasing 1 2
                    cache[i][0] += 1
                    total += cache[j][0]
                        
                elif currNum > num: #decreasing
                    cache[i][1] += 1
                    total += cache[j][1]
                            
        return total
                    
                        

                
        
        