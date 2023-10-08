# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ansList = []
        def dfs(node,ans,sm):
            nonlocal ansList
            if node == None:
                return 0
            
            sm += node.val
            ans.append(node.val)
            if node.left == None and node.right == None:
                if sm == targetSum:
                    ansList.append(list(ans))
            
            dfs(node.left,ans,sm)
            dfs(node.right,ans,sm)
            
            sm -= node.val
            ans.pop()
            
        
        dfs(root,[],0)
            
        return ansList
                
                