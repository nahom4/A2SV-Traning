class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        #go from the back and go from the front and check if the values are equal
        i = 0
        j = len(arr)-1
        
        for i in range(len(arr)-1):
            
            if arr[i]<arr[i+1]:
                pass
                
            else:
                break
        for j in range(len(arr)-1,0,-1):
            if arr[j]< arr[j-1]:
                pass
            else:
                break
                
        if i == j:
            return True
        else:
            return False
        