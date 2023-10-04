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
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            count = left + right 
            if node.val == p.val or node.val == q.val:
                count += 1
                
            if count == 2:
                self.ans = node
                return 0
            return count 
        dfs(root)
        return self.ans
                
            
            
        