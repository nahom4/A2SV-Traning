# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        ans = set([root])
        def dfs(node):
            if not node:
                return 
  
            if node.val in to_delete:
                if node in ans:
                    ans.remove(node)
                if node.left:
                    ans.add(node.left)
                if node.right:
                    ans.add(node.right)
                    
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                return None
            
            return node

        dfs(root)
        return ans

        