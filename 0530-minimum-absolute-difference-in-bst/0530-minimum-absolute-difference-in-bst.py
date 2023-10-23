# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float("inf")
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node == None:
                return float("inf"),float("-inf")
            
            
            mnL,mxL = dfs(node.left)
            mnR,mxR = dfs(node.right)
            
            self.ans = min(self.ans,abs(node.val - mxL), abs(mnR - node.val))
            
            return min(mnL,node.val),max(mxR,node.val)
        
        dfs(root)
        
        return self.ans
        