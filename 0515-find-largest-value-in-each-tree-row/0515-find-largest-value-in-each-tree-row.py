# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #to access each level I would need to use Bfs
        
        if root == None:
            return []
        queue = deque([root])
        ans = []
        while queue:
            
            size = len(queue)
            maxNum = float("-inf")
            for _ in range(size):
                node = queue.popleft()
                maxNum = max(maxNum,node.val)
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                
            ans.append(maxNum)
            
        return ans
                
        