# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        # I do a dfs at every node I check the grand children of the node if the node it self is even
        # I add the grand children and I then continue
        self.res = 0
        def grand_child(node):
            
            if node:
                if node.left:
                    self.res += node.left.val
                if node.right:
                    self.res += node.right.val
            return None,None
            
        
        def dfs(node):
            
            if not node:
                return
            
            if node.val % 2 == 0:
            
                left = node.left
                right = node.right
                
                grand_child(left)
                grand_child(right)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.res
                
            
            
            
            
            
            