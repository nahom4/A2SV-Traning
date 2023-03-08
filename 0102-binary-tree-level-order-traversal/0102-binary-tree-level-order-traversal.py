# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
            self.container = defaultdict(list)
     
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        
        def bfs(root,level):
        
            if not root:
                return None
            
            bfs(root.left,level + 1)
            self.container[level].append(root.val)
            bfs(root.right,level + 1)
            
        bfs(root,0)
        result = []
        self.container = dict(sorted(self.container.items()))
        for key in self.container:
            result.append(self.container[key])
        return result
            
        
        
    
        
        
        