class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        heap = []
        ans = []
        N = len(tasks)
        for i in range(N):
            tasks[i] = [tasks[i][1],i,tasks[i][0]] # change order
            
        tasks.sort(key= lambda x : x[2])
        
        right = 0
        clock = 0
        
        while right < N or heap:
           
            if heap:
                duration,index,start = heapq.heappop(heap)
                ans.append(index)
                clock += duration
                
            else: # cpu is idle
                clock = tasks[right][2]
                
            while right < N and  tasks[right][2] <= clock:
                heapq.heappush(heap,tasks[right])
                right += 1
                
        return ans
                
            
                
        
        