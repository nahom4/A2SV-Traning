class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        lis = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        lis.sort(reverse=True)
        return sum(lis[: k])
        
        
        
        