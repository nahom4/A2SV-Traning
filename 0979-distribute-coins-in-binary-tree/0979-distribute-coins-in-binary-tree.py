# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node == None:
                return [0,0,0] #coins needs ans
            
            coins = node.val
            lc,ln,la = dfs(node.left)
            rc,rn,ra = dfs(node.right)
            
            tc = lc + rc + coins
            tn = ln + rn + 1
          
            diff = tc - tn
            if diff >= 0:
                tc -= tn
                tn = 0
                
            else:
                tn -= tc
                tc = 0

            ta = la + ra + max(tc,tn)
            
            return [tc,tn,ta]
        
        _,_,ans = dfs(root)
        
        return ans
            
            
        