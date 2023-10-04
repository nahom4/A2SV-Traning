# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        #bfs
        queue = deque([root])
        maxLevel = maxSum = float("-inf")
        level = 1
        while queue:
            
            size = len(queue)
            currSum = 0
            for _ in range(size):
                node = queue.popleft()
                currSum += node.val
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
        
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = level
            
            level += 1
            
        return maxLevel
                
            
                    
                
                
            
        