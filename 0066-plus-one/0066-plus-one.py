class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        sm = digits[-1]+ carry + 1 
        if  sm <= 9:

            digits[-1] = sm
        else:
            digits[-1] = sm -10
            carry = 1
        for i in range(len(digits)-2,-1,-1):
       
            
            if digits[i] + carry <= 9:
            
                digits[i] = digits[i]+carry
                carry = 0
            else:
                digits[i] = digits[i]+carry - 10
                carry = 1
            
            
            
         
        if carry != 0:
            digits.insert(0,carry)
        return digits

    