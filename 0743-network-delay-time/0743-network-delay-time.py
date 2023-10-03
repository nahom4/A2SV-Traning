class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #dijkstara from the table return the max value
        minTime = [float("inf")] * (n + 1)
        visited = set()
        priorityQueue = [(0,k)]
        minTime[k] = 0
        minTime[0] = 0
        graph = defaultdict(list)
        for start,end,w in times:
             graph[start].append((end,w))
                
        while priorityQueue:
            w,node = heapq.heappop(priorityQueue)
            if node in visited:
                continue
                
            visited.add(node)
            
            for child,currW in graph[node]:
                currW += w
                if minTime[child] > currW:
                    minTime[child] = currW
                    heapq.heappush(priorityQueue,(currW,child))
   
        return -1 if max(minTime) == float("inf") else max(minTime)
        