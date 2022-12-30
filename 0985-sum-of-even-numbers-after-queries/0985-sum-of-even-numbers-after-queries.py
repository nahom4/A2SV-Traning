class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        #prepare the sum of even numbers of num
        
        even_sum = 0
        
        for element in nums:
            if element%2 == 0:
                even_sum += element
                

        
        even_list =  []
        
        for query in queries:
            access = query[1]
            value = query[0]
            total = 0
          
            if nums[access] %2 == 0:
           
                
              
                even_sum -= nums[access] 
          
                
            nums[access] = nums[access] + value
        
            if nums[access] %2 == 0:
                even_sum += nums[access] 
          
            even_list.append(even_sum)
                
        return even_list
                
            
        