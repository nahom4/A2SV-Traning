# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        ans = []
        def path(root):
            if not root:
                return
            
            ans.append(str(root.val)) 
            if not root.right and not root.left:
                result.append('->'.join(ans))
                
                
               
            path(root.left)
            path(root.right)
            ans.pop()
        path(root)
        
        return result
                
            