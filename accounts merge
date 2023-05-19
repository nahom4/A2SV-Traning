class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # thinking of a brute force approach
        n = len(accounts)
        parent =[i for i in range(n)]
        size = [1 for i in range(n)]
        emails = {}
        
        # rep = {i : i for i in range(n)}
        # /size = {i : 1 for i in range(n)}
        
#         def same_account(first,second):
            
#             return any([email in accounts[second] for email in accounts[first]])
        
        def find(node):
            
            if node == parent[node]:
                return node
            
            parent_value = find(parent[node])
            parent[node] = parent_value
            return parent_value
        
        def union(email,index):
            
            if not email in emails:
                emails[email] = index
            
            else:
                firstParent = find(emails[email])
                secondParent = find(index)

                if firstParent == secondParent:
                    return 

                if size[firstParent] < size[secondParent]:
                    firstParent,secondParent = secondParent,firstParent
                    
                size[firstParent] += size[secondParent]
                parent[secondParent] = firstParent
                
          
                
        for index,email_list in enumerate(accounts):
            for email in email_list[1:]:
                union(email,index)
                
        
        #process
        res = []
        temp = defaultdict(list)
        for email in emails:
            
            node = find(emails[email])
            temp[node].append(email)
            
        
        for key in temp:
            lis = sorted(temp[key])
            lis.insert(0,accounts[key][0])
            res.append(lis)
        
        return res
        
        
    
                
            
            
            
        