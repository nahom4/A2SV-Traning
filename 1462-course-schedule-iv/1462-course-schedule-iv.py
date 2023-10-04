class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        grid = [[float("inf")] * numCourses for _ in range(numCourses)]
    
        for preReq,course in prerequisites:
            grid[preReq][course] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    grid[i][j] = min(grid[i][j],(grid[i][k] + grid[k][j]))
                    
        ans = []
        for preReq,course in queries:
            if grid[preReq][course] == float("inf"):
                ans.append(False)
            else:
                ans.append(True)
                
        return ans
                    
                    
            
            
            
        
        
        
       
                    
        
        