class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #it is count the number of islands problem
        count = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            #find it's neigbhors
            for col in range(len(isConnected)):
                if isConnected[node - 1][col] == 1 and not (col + 1) in visited:
                    dfs(col + 1)
                    
        for node in range(1,len(isConnected) + 1):
            if node not in visited:
                count += 1
                dfs(node)
            
        return count
                
                
        