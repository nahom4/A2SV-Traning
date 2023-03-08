# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mx_hight = 0
        result = []
        def right_side(root,level):
            nonlocal mx_hight
            if not root:
                return None
            if level > mx_hight:
               
                result.append(root.val)
                mx_hight = level
            
            right_side(root.right,level + 1)
            
            right_side(root.left,level + 1)
        right_side(root,1)
    
        return result
                
            
            
        