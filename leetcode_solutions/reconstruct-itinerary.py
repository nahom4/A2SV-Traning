class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        """
         let's do a kind of dfs whenever a person takes a flight we remove it                   connetion with that city whatever result the cities return we take the
         let's build a directed graph
        """
        tickets.sort()
        graph = defaultdict(deque)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
            
        N = len(tickets)
        cities = []
        def dfs(city,noTickets):
            
            if noTickets != N and not graph[city]:
                return False
            if noTickets == N and not graph[city]:
                return True
            
            itenery = None
            count = len(graph[city])

            while count > 0:
                child = graph[city].popleft()
                res = dfs(child,noTickets + 1)    
                cities.append(child)
                if res:
                    return res
                graph[city].append(child)
                cities.pop()
                count -= 1
                
            return False
                
        dfs('JFK',0)
        return ["JFK"] + cities[:: -1 ]
                
                
                
                