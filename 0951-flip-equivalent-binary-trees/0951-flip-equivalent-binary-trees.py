# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(firstNode,secondNode):
            
            if firstNode == None and secondNode == None:
                return True
            
            if firstNode == None or secondNode == None:
                return False
            
            
            if firstNode.val != secondNode.val:
                return False
            
            if dfs(firstNode.left,secondNode.left) and dfs(firstNode.right,secondNode.right):
                return True
            
            if dfs(firstNode.right,secondNode.left) and dfs(firstNode.left,secondNode.right):
                return True
            
            return False
        
        return dfs(root1,root2)
    
        