# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_node = root.left
        right_node = root.right
        
        def symmetric(left_node,right_node):
            
            if not left_node and not right_node:
                return True
            
            #for the left tree we do a left first traversal and for the right tree we do a
            #right first traversal
            
            if bool(left_node) ^ bool(right_node):
               
                return False
            
            if left_node.val == right_node.val:
                return symmetric(left_node.left,right_node.right) and symmetric(left_node.right,right_node.left)
            else:
                
                return False
            
        return symmetric(left_node,right_node)
            
         
            
            
            
            
        
       
        
        
            
            
            
            
        
        
        
        
        