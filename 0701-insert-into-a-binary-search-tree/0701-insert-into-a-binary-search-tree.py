# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, nahom: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #first you have to search
     
            root = nahom
            if root == None:
                return TreeNode(val)
            
            if root.val < val and root.right == None:
                root.right = TreeNode(val)

            if root.val > val and root.left == None:
                root.left = TreeNode(val)

            if root.val < val:
                self.insertIntoBST(root.right, val)

            else:
                self.insertIntoBST(root.left, val)
            
            
            


            return nahom
      
            
        