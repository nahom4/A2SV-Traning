from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        # Build a graph where the edges are sorted lexicographically
        graph = defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            graph[ticket[0]].append(ticket[1])
        
        def dfs(node):
            # Visit all destinations from the current airport
            while graph[node]:
                next_dest = graph[node].pop()
                dfs(next_dest)
            # Add the current airport to the itinerary
            result.append(node)
        
        result = []
        dfs("JFK")
        # Reverse the result to get the correct itinerary
        return result[::-1]
