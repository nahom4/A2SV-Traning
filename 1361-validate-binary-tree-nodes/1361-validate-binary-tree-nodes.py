class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # a valid binary tree is the same as a valid tree
        """
            a tree is valid if it is acyclic and and doesn't containd disconnected
            components to check this we will use union find
            
        """
        
        rep = {i : i for i in range(n)}
        rank = {i : 1 for i in range(n)}
        
        def find(node):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        
        def union(firstNode,secondNode,components):
            
            firstNodeParent,secondNodeParent = find(firstNode),find(secondNode)
            
            if firstNodeParent == secondNodeParent or secondNodeParent != secondNode:
                return False,components
            
            rep[secondNodeParent] = firstNodeParent
            components -= 1
            return True,components
                
            
        components = n - 1
        for i in range(n):
            validLeft = True
            if leftChild[i] != -1:
                validLeft,components = union(i,leftChild[i],components)
              
            validRight = True
            if rightChild[i] != -1:
                validRight,components = union(i,rightChild[i],components)
                
            
            if not validRight or not validLeft:
                return False
            
        
        print(components)
        if components == 0:
            return True
        