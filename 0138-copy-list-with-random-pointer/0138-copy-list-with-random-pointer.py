"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeMap = {}
        curr = head
        newHead = Node(-1)
        res = newHead
        while curr:
        
            newNode = Node(curr.val,curr.next,curr.random)
            if curr in nodeMap:
                newNode = nodeMap[curr]
              
            nodeMap[curr] = newNode
            randomNode = None
            if curr.random:
                randomNode = Node(curr.random.val,curr.random.next,curr.random.random)
                if curr.random in nodeMap:
                    randomNode = nodeMap[curr.random]
                    
                else:
                    nodeMap[curr.random] = randomNode 
                
            newNode.random = randomNode
            newHead.next = newNode
            curr = curr.next
            newHead = newNode
            
        return res.next

        
            
        