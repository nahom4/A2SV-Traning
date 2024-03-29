class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        Mod = 10 ** 9 + 7
        odd = n // 2
        even = odd + n % 2
        
        return ((pow(5,even,Mod)) * (pow(4,odd,Mod))) % Mod

        
#         def power(num,pw):
            
#             if pw == 0:
#                 return 1
#             if pw == 1:
#                 return num
            
#             if pw % 2 == 0:        
#                 return ((power(num,pw // 2) % Mod) ** 2 ) % Mod
        
#             else:
#                 return ((power(num,pw // 2) % Mod ) ** 2 % Mod * num ) % Mod
        
            
        
        