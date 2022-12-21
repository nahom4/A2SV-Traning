class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #select all the valid elements
        valid = []
        for i, values in enumerate(points):
           
            first, second = values
            if first == x or second == y:
                valid.append((values,i))
                

        
        # calculate manhattan distance for the valid elements
        man = []
        for element in valid:
            cord, index = element
         
            x_distance=cord[0]
            y_distance = cord[1]
         
            value = ((abs(x - x_distance) + abs(y - y_distance)),index)
            
            man.append(value)
        
     
        man.sort()
        if man:
            result,nm = man[0]
        else:
            return -1
    
        return nm
            
                