class Solution:
    def spiralOrder(self, matrix):
        # since it is a matrix nested loop is the only way solve the problem
        rowbg = 0
        rowend = len(matrix)-1
        columnbg = 0
        columend = len(matrix[0])-1
        arr = []
        if len(matrix) == 0:
            return matrix
       

        while rowbg <= rowend and columnbg <= columend:  # should controll the spiral with in a spiral
            
            for y in range(columnbg, columend+1):# row
              

                arr.append(matrix[rowbg][y])
            rowbg += 1
    
            for m in range(rowbg, rowend+1):  # column
                    arr.append(matrix[m][columend])    
            columend -= 1
            if rowbg <= rowend:
                for v in range(columend,columnbg-1,-1):
                    arr.append(matrix[rowend][v])
            rowend -= 1
            if columnbg <= columend:
                for w in range(rowend,rowbg-1,-1):
                    arr.append(matrix[w][columnbg])
            columnbg += 1

        return arr