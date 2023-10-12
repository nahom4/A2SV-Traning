# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        visited = defaultdict(int)
        ans = []
        def dfs(node):
            if node == None:
                return " "
            
            currString = ""
            
            currString += str(node.val) + ","
            currString += dfs(node.left)
            currString += dfs(node.right)
 
            if visited[currString] == 1:
                ans.append(node)
                
            visited[currString] += 1
            
            return currString
           
        dfs(root)
        return ans
            
            
        