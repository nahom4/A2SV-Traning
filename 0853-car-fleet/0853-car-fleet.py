class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #let's calculate the time take to reach their destination
        for i,x in enumerate(position):
            speed[i] = (target - position[i])/speed[i]
      
        #dictionary to remember position after sorting
        
        dic = dict()
        for i in range(len(position)):
            
            dic[position[i]] = i
  
        position.sort(reverse=True)
        
        #let's build our decreasing stack
        stack = []
        count = 0
        
        for x in position:
            flag = False
           
            while stack and stack[-1 ] < speed[dic[x]]:
                stack.pop()
                flag = True
            
            if flag:
                count += 1
            if not stack:
                stack.append(speed[dic[x]])
            else:
                stack.append(stack[-1])
        if stack:
            count += 1
        return count
                
            
        