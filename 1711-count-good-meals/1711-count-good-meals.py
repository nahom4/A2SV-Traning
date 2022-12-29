class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        # There are only 20 powers of 2 2**20
        count = Counter(deliciousness)
        power = [2**n for n in range(22)]
        total = 0
        
      
        
        for x in deliciousness:
            count[x]-=1
            for y in power:
             
                diff = y - x
                total+=count.get(diff,0)
                
        return total%(10**9 + 7)
            
        
        
        
        