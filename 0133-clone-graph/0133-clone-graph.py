"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodeMap = {}
        
        def dfs(node,copyNode):
            
            newList = []
            if  node in nodeMap:
                return nodeMap[node]
              
            if not node:
                return
            copyNode.val  = node.val
            nodeMap[node] = copyNode
            
            for child in node.neighbors:

                currValue = dfs(child,Node())
                newList.append(currValue)
                
            copyNode.neighbors = newList
            return copyNode
        
        return dfs(node,Node())