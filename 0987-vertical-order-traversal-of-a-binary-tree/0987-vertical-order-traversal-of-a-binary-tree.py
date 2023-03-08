# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.container = defaultdict(list)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def virtical(root,col,row):
            
            if not root:
                return None
            
            virtical(root.left, col - 1,row + 1)
          
            self.container[col].append((row,root.val))
            virtical(root.right,col + 1,row + 1)
            
        virtical(root,0,0)
        self.container = dict(sorted(self.container.items()))
        for key in self.container:
            self.container[key].sort()
            
        result = []
        
        for key in self.container:
            temp = []
            for val in self.container[key]:
                left,right = val
                temp.append(right)
                
            result.append(temp)
        return result
        
        
        