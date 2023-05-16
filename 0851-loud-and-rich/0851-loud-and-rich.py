class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        #I need to collect all the people who are richer than the person
        #It is just like collecting all ancestors
        
        richer_people = [set() for _ in range(len(quiet))]
        queue = deque()
        graph = defaultdict(list)
        in_degree = [0] * len(quiet)
        
        for start,end in richer:
            graph[start].append(end)
            in_degree[end] += 1
          
     
        for person in range(len(in_degree)):
            if in_degree[person] == 0:
                queue.append(person)
                    
        while queue:
            curr = queue.popleft()
          
            for child in graph[curr]:
                
                richer_people[child].add(curr)
                richer_people[child].update(richer_people[curr])
                
                in_degree[child] -= 1
                
                if in_degree[child] == 0:
                    queue.append(child)
                    
        ans = []
        for index,group in enumerate(richer_people):
            quietest = quiet[index]
            pr = index
            for person in group:
                if quiet[person] < quietest:
                    quietest = quiet[person]
                    pr = person
                                  
            ans.append(pr)
                
        return ans
                
                
            
            
        
        