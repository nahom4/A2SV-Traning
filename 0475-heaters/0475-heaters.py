class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        # it seems to be a two pointer problem
        houses.sort()
        heaters.sort()
        N = len(houses)
        heater = 0 
        curr,currMin = float("inf"),float("-inf") 
        H = len(heaters)
        for i in range(N):
            house = houses[i]
            
            while heater < H and house >= heaters[heater]:
                curr = heaters[heater]
                heater += 1
      
            back = abs(house - curr)
            front = heaters[heater] - house if heater < len(heaters) else float("inf")
            currMin = max(min(back,front),currMin)
            
            
        return currMin
                
            
                
            
            
        