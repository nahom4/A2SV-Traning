class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.graph = defaultdict(list)
        self.parent = parent
        n = len(parent)
        for i in range(n):
            if parent[i] != -1:
                self.graph[parent[i]].append(i)
                
        self.nodeOwner = [-1] * n
        
    def lock(self, num: int, user: int) -> bool:
        if self.nodeOwner[num] == -1:
            self.nodeOwner[num] = user
            return True

    def unlock(self, num: int, user: int) -> bool:
        if self.nodeOwner[num] == user:
            self.nodeOwner[num] = -1
            return True
        
    def upgrade(self, num: int, user: int) -> bool:
        
        if self.nodeOwner[num] != -1:
            return False
        
        if not self.checkDescendants(num):
            return False
        
        if self.checkAncestor(num):
            return False
        
        self.unlockDescendants(num)
        self.nodeOwner[num] = user
        
        return True
            
    def checkDescendants(self,node):
        
        isLocked = False
        isLocked = isLocked or self.nodeOwner[node] != -1
        
        for child in self.graph[node]:
            isLocked = isLocked or self.checkDescendants(child)
            
        return isLocked
    
    def checkAncestor(self,node):
        
        isLocked = False
        while node != -1:
            isLocked = isLocked or self.nodeOwner[node] != -1
            node = self.parent[node]
            
        return isLocked
        
    def unlockDescendants(self,node):
        
        self.nodeOwner[node] = -1 
        for child in self.graph[node]:
            self.unlockDescendants(child)
            
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)