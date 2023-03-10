# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.mode = Counter()
        self.mx = 1
        def mode(root):
            if not root:
                return None, 0

            mode(root.left)

            self.mode[root.val] += 1
          
            if self.mode[root.val] == self.mx:
                self.result.append(root.val)
            if self.mode[root.val] > self.mx:
                self.mx = self.mode[root.val]
                self.result = []
                self.result.append(root.val)

            mode(root.right)
        
        mode(root)
        
        return self.result
                
                

            
        