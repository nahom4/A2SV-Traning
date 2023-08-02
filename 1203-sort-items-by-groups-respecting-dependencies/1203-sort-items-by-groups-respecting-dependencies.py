class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def topologicalSort(nodeList):
            graph = defaultdict(list)
            n = len(nodeList)
            queue = deque()
            ans = []
            visited = set()
            in_degree = [0] * n
            
            for index,beforeList in enumerate(nodeList):
                for value in beforeList:
                    graph[value].append(index)
                in_degree[index] += len(beforeList)
            
            for index in range(n):
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
               
            return ans if len(ans) == len(graph) else []

        # sort the groups 
        for index,groupIndex in enumerate(group):
            if groupIndex == -1:
                group[index] = m
                m += 1
        groupGraph = [set() for _ in range(m)]
       
        for index,beforeList in enumerate(beforeItems):
            indexGroup = group[index]
            for value in beforeList:
                valueGroup = group[value]
                if valueGroup == indexGroup:
                    continue
                groupGraph[indexGroup].add(valueGroup)
                
        groupSort = topologicalSort(groupGraph)
        individualSort = topologicalSort(beforeItems)
        
        ans = [[] for _ in range(m)]
        finalAnswer = []
        if groupSort and individualSort:
            for item in individualSort:
                ans[group[item]].append(item)
             
            for groupName in groupSort:
                finalAnswer.extend(ans[groupName])
                
        return finalAnswer
            
            
                
                
            
        
      

                
        