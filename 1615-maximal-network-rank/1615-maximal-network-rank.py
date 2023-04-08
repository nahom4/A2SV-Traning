class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        #create adjecency list
        
        graph = defaultdict(list)
        
        for road in roads:
            start,end = road
            graph[start].append(end)
            graph[end].append(start)
            
        total = []
        for key in graph:
            lst = graph[key]
            lst.append(key)
            total.append(lst)
            
        
        res = 0
        for i in range(len(total)):
            for j in range(len(total)):
                
                if i == j:
                    continue
                
                if total[i][-1] in total[j]:
                    res = max(res,(len(total[i]) + len(total[j]) - 3))
                else:
                     res = max(res,(len(total[i]) + len(total[j]) - 2))
  
        
        return res