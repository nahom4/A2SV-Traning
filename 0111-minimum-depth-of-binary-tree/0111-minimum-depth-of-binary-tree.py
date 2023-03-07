# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        left_hight = self.minDepth(root.left)
        right_hight = self.minDepth(root.right)
            
        if left_hight == 0:
            return 1 + right_hight
           
        elif right_hight == 0:
            return 1 + left_hight
        else:
            return 1 + min(left_hight,right_hight)
        
        