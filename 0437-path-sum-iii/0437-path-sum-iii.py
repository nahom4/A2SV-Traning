# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ct = Counter()
        ct[0] = 0
        def dfs(node,sm):
            
            if not node:
                return 0
            
            sm += node.val
            count = 0
            for key in ct:
                if sm - ct[key] == targetSum:
                    count += 1
        
            ct[node] = sm
            left = dfs(node.left,sm)
            right = dfs(node.right,sm)
            ct.pop(node)
            count += left + right
            return count
        
        return dfs(root,0)
        