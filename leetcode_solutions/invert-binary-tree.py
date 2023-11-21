# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if node == None:
                return 

            left = node.left
            right = node.right
            dfs(left)
            dfs(right)
            node.left = right
            node.right = left

        dfs(root)
        return root
        