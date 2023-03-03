class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(row,row_index):
            
            if row_index == 0:
                return row
            new = []
            for i in range(len(row) - 1):
                new.append(row[i] + row[i + 1])
            new.insert(0,1)
            new.append(1)
            
            return pascal(new,row_index - 1)
        
        return pascal([1],rowIndex)
                
            
            
            
            
            
            
        