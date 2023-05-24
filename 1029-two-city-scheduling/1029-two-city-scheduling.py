class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs,key= lambda value : value[0] - value[-1])
        
        A = costs[: len(costs) // 2]
        B = costs[len(costs) // 2 : ]
        
        total = 0
        
        for value in A:
            total += value[0]
            
        for value in B:
            total += value[1]
            
        return total
        