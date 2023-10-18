class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        inDegree = [0] * n
        updatedTime = list(time)
        for preReq,course in relations:
            graph[preReq].append(course)
            inDegree[course - 1] += 1
            
        queue = deque()
        
        for i in range(n):
            if inDegree[i] == 0:
                queue.append((i + 1,time[i]))
                
        timeLine = 0
        while queue:
            node,timeFrame = queue.popleft()
            timeLine = max(timeLine,timeFrame)
            for child in graph[node]:
                
                inDegree[child - 1] -= 1
                updatedTime[child - 1] = max(updatedTime[child - 1],time[child - 1] + timeFrame)
            
                if inDegree[child - 1] == 0:
                    
                    queue.append((child,updatedTime[child - 1]))
                
        return timeLine
            
        