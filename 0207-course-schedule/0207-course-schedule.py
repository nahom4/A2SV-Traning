class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build the graph
        graph = defaultdict(list)
        queue = deque()
        ans = []
        visited = set()
        in_degree = [0] * numCourses
        
        for course,pre in prerequisites:
        
            graph[pre].append(course)
            in_degree[course] += 1
            
        
        for index in range(numCourses):
            if in_degree[index] == 0:
                queue.append(index)
    
        while queue:
            
            node = queue.popleft()
            ans.append(node)
            
            for child in graph[node]:
                if not child in visited:
                    in_degree[child] -= 1

                    if in_degree[child] == 0:
                        queue.append(child)
                        visited.add(child)
                 
        return len(ans) == numCourses

            
                
            
       
        