# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        #we do dfs and at the bottom we pass the max value each time registering
        #the the absolute max
        self.result = float('-inf')
        def dfs(node):
            
            if not node:
                return 0
            
            curr_max = node.val
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            new_left = node.val
            new_right = node.val
            
            if left_max > 0:
                curr_max += left_max
                new_left += left_max
                
            if right_max > 0:
                curr_max += right_max
                new_right += right_max
          
            self.result  = max(self.result,curr_max)
            return max(new_left,new_right)
        
        dfs(root)
        return self.result
            
            
        