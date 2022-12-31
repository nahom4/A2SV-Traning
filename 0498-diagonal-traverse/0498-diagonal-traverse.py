class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        store =  defaultdict(list)
        final = []
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                store[row+col].append(mat[row][col])
    
                
        for value in store:
            if value%2 != 0:
                for num in store[value]:
                    final.append(num)
            else:
                
                for i in range(len(store[value])-1,-1,-1):
                    final.append(store[value][i])
                
                
                
        return final
        