#User function Template for python3

class Solution: 
    def select(self, arr, i):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i],arr[i - 1] = arr[i -1], arr[i]
            i -= 1
            
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            self.select(arr,i)
        return arr
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends