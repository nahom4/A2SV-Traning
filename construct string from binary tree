# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        lis = []
        def preorder(root):
            
            if not root:
                return
             
            lis.append(str(root.val))
            if not root.left and not root.right:
                return
            
            lis.append('(')
            preorder(root.left)
            lis.append(')')
            
            if not root.right:
                return
            
            lis.append('(')
            
            preorder(root.right)
            
            lis.append(')')
        preorder(root)
        return ''.join(lis)