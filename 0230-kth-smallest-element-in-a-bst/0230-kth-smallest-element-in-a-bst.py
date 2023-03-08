# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0
        
        def smallest(root,k):
            nonlocal count
            nonlocal result
            if root == None:
              
                return count

            smallest(root.left,k)
            count += 1
            if count == k:
                result = root.val
            smallest(root.right,k)
            
           
        
        smallest(root,k)
        return result 
        
            
        
            

        