#User function Template for python3

class Solution:
    def heapPop(self,arr):
        value = arr[0]
        arr[0],arr[-1] = arr[-1],arr[0]
        arr.pop()
        if arr:
            self.heapify(arr,len(arr),0)
        return value
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # here we should use heapify down
        
        parent = i
        smaller_value = i
        first_child = parent * 2 + 1
        second_child = parent * 2 + 2
        
        while parent < n:
            
            if first_child < n and arr[smaller_value] > arr[first_child]:
                smaller_value = first_child
                
                
            if second_child < n and  arr[smaller_value] > arr[second_child]:
                smaller_value = second_child
               
                
            if smaller_value  != parent:
                arr[smaller_value],arr[parent] = arr[parent],arr[smaller_value]
                parent = smaller_value
            else:
                break
            
            first_child = parent * 2 + 1
            second_child = parent * 2 + 2
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # To build the heap we could use o(n) algorithm
        
        for i in range((n // 2 - 1),-1,-1):
            
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        sorted_list = []
        self.buildHeap(arr,len(arr))
        
        while arr:
            sorted_list.append(self.heapPop(arr))
            
        for val in sorted_list:
            arr.append(val)
        # print(*sorted_list)
        # return sorted_list
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends