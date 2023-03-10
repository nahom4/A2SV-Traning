# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def average(root):
            if not root:
                return (0,0)
     

            left_size,left_val = average(root.left)
            right_size,right_val = average(root.right)
            size = (left_size + right_size + 1)
            value = (left_val + right_val + root.val)
            if root.val == value//size :
                self.count += 1

            return (size,value)
        average(root)
    
        return self.count
            
            
            
        