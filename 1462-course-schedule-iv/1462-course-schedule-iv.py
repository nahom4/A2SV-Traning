class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        visited = set()
        in_degree = [0] * numCourses
        queue = deque()
        dependancy = [set() for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1
       
        for index in range(numCourses):
            if in_degree[index] == 0:
                queue.append(index)
                
        
        while queue:
            node = queue.popleft()
            
            for child in graph[node]:
               
                dependancy[child].add(node)
                dependancy[child].update(dependancy[node])
                if not child in visited:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)
                        visited.add(child)

        answer = []
        
        for a,b in queries:
            if a in dependancy[b]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
                