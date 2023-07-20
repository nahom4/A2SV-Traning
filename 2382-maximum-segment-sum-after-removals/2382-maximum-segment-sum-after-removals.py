class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        rep = {i : i for i in range(n)}
        size = {i : 1 for i in range(n)}
        sm = {i : 0 for i in range(n)}
        def find(node):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(node1,node2):
            first_parent,second_parent = find(node1),find(node2)
            
            if first_parent == second_parent:
                return 
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
                
            size[first_parent] += size[second_parent]
            rep[second_parent] = first_parent
            sm[first_parent] += sm[second_parent]
        
        answer = [0]
        max_sum = 0
        
        for i in range(n - 1,0,-1):
            index = removeQueries[i]
            sm[index] = nums[index]
          
            if index - 1 >= 0 and sm[index - 1]:
                union(index,index - 1)
              
            if index + 1 < n and sm[index + 1]:
                union(index, index + 1)
              
            parent = find(index)   
            total = sm[parent]
            max_sum = max(total,max_sum)
            answer.append(max_sum)
        return answer[:: -1]
            
        