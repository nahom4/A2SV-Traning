class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        # at each point we can either add or remove 3 or 5 jugs of water
        choices = [jug1Capacity,-jug1Capacity,jug2Capacity,-jug2Capacity]
        visited = set()
        def dfs(total):
         
            if total == targetCapacity:
                return True
            if total in visited or total < 0 or total >  jug1Capacity + jug2Capacity:
                return False
            
            visited.add(total)    
            valid = False
            for choice in choices:
                valid = valid or dfs(total + choice)
            
            return valid
            
        return dfs(0)
        