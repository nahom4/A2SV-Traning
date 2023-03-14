# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root):
            if not root.left and root.right:
                right_mx,right_min,right_valid = valid(root.right)
                if right_valid and  root.val < right_min:
                    return (right_mx,root.val,True)
                return (right_mx,root.val,False)
                
            if not root.right and root.left:
                left_max,left_min,left_valid = valid(root.left) 
                    
                if left_valid and root.val > left_max :
                    return (root.val,left_min,True)
                return (root.val,left_min,False)
            if not root.left and not root.right:
                return (root.val,root.val,True)

            left_max,left_min,left_valid = valid(root.left)
            right_mx,right_min,right_valid = valid(root.right)
        
                
            if left_valid and right_valid and root.val > left_max and root.val < right_min:
                return (max(left_max,right_mx),min(left_min,right_min),True)
            
            return (max(left_max,right_mx),min(left_min,right_min),False)

       
        left,right,valid = valid(root)

        return valid