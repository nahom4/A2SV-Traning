class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        #let's build a sort of graph
        graph = dict()
       
        for i,equation in enumerate(equations):
            A,B = equation
            value = values[i]
            if not A in graph:
                graph[A] = dict()
                
            if not B in graph:
                graph[B] = dict()
                
            graph[A][B] = value
            graph[B][A] = 1 / value
           
        ans = []
        for query in queries:
            A,B = query
            visited = set()
            
            def dfs(letter,target):
                
                if not letter in graph:
                    return -1
                if letter == target:
                    return 1
                if letter in visited:
                    return float("-inf")
                visited.add(letter)
                maxValue = -1
                for child in graph[letter]:
                    maxValue = max(maxValue, graph[letter][child] *dfs(child,target))
                return maxValue
            
            val = dfs(A,B)
            ans.append(val if val >= 0 else float(-1))
            
        return ans
            
            
                    
                
                
            
            
        