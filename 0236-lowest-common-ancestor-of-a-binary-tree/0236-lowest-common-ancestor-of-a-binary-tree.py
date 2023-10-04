# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node == None:
                return False 
            left = dfs(node.left)
            right = dfs(node.right)
            
            count = 0
            if left:
                count += 1
            if right:
                count += 1
                
            if node.val == p.val or node.val == q.val:
                count += 1
                
            if count == 2:
                self.ans = node
                return False
            
            if count >= 1:
                return True
        dfs(root)
        return self.ans
                
            
            
        