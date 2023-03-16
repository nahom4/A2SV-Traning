# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = deque([(root,0)])
        mx_width = 0
        
        def width(level,mx_width):
            
            if not level:
                return mx_width
            
            _,left = level[0]
            _,right = level[-1]
            mx_width = max(mx_width,right - left + 1)
            
            for _ in range(len(level)):
                node, index = level.popleft()
                if node.left:
                    level.append((node.left, 2 * index))
                if node.right:
                    level.append((node.right, 2 * index + 1))
                    
            return width(level,mx_width)
            
        return width(level,mx_width)
                    
            
                    
                
            
            
            
            
            
        