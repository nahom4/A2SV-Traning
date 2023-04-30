# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #turn the tree in to a graph and do bfs on the graph starting from the target
        
        graph = defaultdict(list)
        
        def dfs(node):
            
            if not node: return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        #now we got the graph let's do bfs
        
        queue = deque()
        queue.append((target.val,0))
        res = []
        visited = set()
        while queue:
            
            node,level = queue.popleft()
            
            if level == k:
                res.append(node)
                
            for neibhor in graph[node]:
                if not neibhor in visited:
                    queue.append((neibhor,level + 1))
                    visited.add(node)
                    
        return res
        
                
                
                
        