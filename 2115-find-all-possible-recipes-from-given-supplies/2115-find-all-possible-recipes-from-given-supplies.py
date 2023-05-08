class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # to form the graph for every value in recipices i check out it's ingridients
        # if a value in the ingredients is in the recipes add it as a child if
        # if elemnt in the ingridient is not in ingridients increase the inward count
        
        queue = deque()
        in_ward = [0] * len(recipes)
        graph = defaultdict(list)
        res = []
        
        for i in range(len(recipes)):
            
            for ingridinet in ingredients[i]:
                if ingridinet in recipes:
                    graph[ingridinet].append((recipes[i],i))
                    in_ward[i] += 1
                    
                else:
                    if not ingridinet in supplies:
                        in_ward[i] += 1
            
        print(graph)
        
        for index, value in enumerate(in_ward):
            if value == 0:
                queue.append((recipes[index],index))
                
        
        while queue:
            
            recipe,index = queue.popleft()
            res.append(recipe)
            
            for child in graph[recipe]:
                child,index = child
                in_ward[index] -= 1
                if in_ward[index] == 0:
                    queue.append((child,index))
                    
        return res
                
            
                    
                
        