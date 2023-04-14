# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        lis = []
        
        def dfs(root):
          
            nonlocal total
          
            
            lis.append(str(root.val)) 
            
            if not root.left and not root.right:
                total += int(''.join(lis))
                return
            if root.left:
                dfs(root.left)
                lis.pop()
            
            if root.right:
                dfs(root.right)
                lis.pop()
            
        dfs(root)
        return total