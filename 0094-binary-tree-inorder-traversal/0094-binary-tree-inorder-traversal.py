# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        
        self.result = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #base case
        if root == None:
            return self.result
        
        #call the left
        self.inorderTraversal(root.left)
        
        self.result.append(root.val)
        
        #call the right
        self.inorderTraversal(root.right)
        
        return self.result
        
        
        