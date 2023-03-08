# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
        def merge(root1,root2):
            
            if not root1 and not root2:
                return None
            
            #Three cases
            if not root1 and root2:
                new_node = TreeNode(root2.val)
                new_node.left = merge(None,root2.left)
                new_node.right = merge(None, root2.right)
            if not root2 and root1:
                new_node = TreeNode(root1.val)
                new_node.left = merge(root1.left,None)
                new_node.right = merge(root1.right,None)
            
            if root1 and root2:
                new_node = TreeNode(root1.val + root2.val)
                new_node.left = merge(root1.left,root2.left)
                new_node.right = merge(root1.right,root2.right)
                
              
            return new_node
        return merge(root1,root2)
                
        
            
            
            
            
        
        
        
        return merge(root1,root2)
        
        
        
        