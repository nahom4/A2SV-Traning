class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        [[],[],[]]
        """
        glasses = [[0] * size for size in range(1,101)]
        glasses[0][0] = poured
        
        for row in range(len(glasses) - 1):
            for col in range(row + 1):
                # print(glasses[row])
                glass = glasses[row][col]
                if glass > 1:
                    #it overflows
                    overflow = glass - 1
                    glasses[row][col] = 1
                    #fill left child
                    glasses[row + 1][col] += overflow / 2.0
                    # fill the right child
                    glasses[row + 1][col + 1] += overflow / 2.0
  
        return glasses[query_row][query_glass]
                    
            
            
        