class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        queue = deque()
        in_degree = [0] * numCourses
        res = []
        
        for pre,course in prerequisites:
            
            graph[course].append(pre)
            in_degree[pre] += 1
            
            
        for index,value in enumerate(in_degree):
            
            if value == 0:
                queue.append(index)
                
                
        while queue:
            
            curr = queue.popleft()
            res.append(curr)
            
            for child in graph[curr]:
                
                in_degree[child] -= 1
                
                if in_degree[child] == 0:
                    queue.append(child)
          
        if len(res) != numCourses:
            return []
        return res
            
                
        