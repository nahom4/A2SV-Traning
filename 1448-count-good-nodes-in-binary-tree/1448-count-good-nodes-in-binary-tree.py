# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxNumber):
            
            if not node:
                return 0
            
            left = dfs(node.left,max(maxNumber,node.val))
            right = dfs(node.right,max(maxNumber,node.val))
            
            total = left + right
            if node.val >= maxNumber:
                total += 1
                
            return total
        
        return dfs(root,float("-inf"))
        