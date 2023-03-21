# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
            
        def add_node(root,node):
            
            if not root:
                return 
            if not root.left:
                if node.val < root.val:
                    root.left = node
                    return
            if not root.right:
                if node.val > root.val:
                    root.right = node
                    return
               
            if root.val < node.val:
                add_node(root.right ,node)
                
            if root.val > node.val:
                add_node(root.left, node)
                
        for i in range(1,len(preorder)):
            new = TreeNode(preorder[i])
            add_node(root,new)
         
        return root
        