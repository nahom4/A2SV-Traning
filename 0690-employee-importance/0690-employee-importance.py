"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        #map the node with it's index
        mp = dict()
        for emp in employees:
            mp[emp.id] = emp
        
        
        def dfs(node):
            
            total = 0
            total += node.importance
            
            for child in node.subordinates:
                total += dfs(mp[child])
                
            return total
             
       
        
        
        return dfs(mp[id])
            
            
        
        
        
        