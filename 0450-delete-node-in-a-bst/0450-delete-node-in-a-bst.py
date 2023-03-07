# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(node):
            current = node
            
            while current.left:
                current = current.left
                
            return current
        
        def delete(root,key):
            
            if root == None:
                return root
        
            #search
            if key > root.val:
                root.right = delete(root.right,key)
                
            elif key < root.val:
                root.left = delete(root.left,key)
                
            else:
                #means we found it
                #case one and two
                if not root.right:
                    return root.left
                if not root.left:
                    return root.right
                
                #case three
                #The node has to childs which means we need to find the inorder predsecor first
                
                temp_node = find_min(root.right)
                
                #now we found the min from right branch
                root.val = temp_node.val
                root.right = delete(root.right,temp_node.val)
                
            return root
        
        return delete(root,key)
            
        
        