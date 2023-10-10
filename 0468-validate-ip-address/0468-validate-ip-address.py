class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        values = {"a","b","c","d","e","f","A","B","C","D","E","F"}
        def ipv4(queryIP):
            ip = queryIP.split(".")
            if not len(ip) == 4:
                return False
            
            for sub in ip:
                
                try:
                    
                    if sub[0] == "0" and len(sub) > 1:
                        return False
                    if not (0 <= int(sub) <= 255):
                        return False
                except:
                    return False
                
            return True
                    
        def ipv6(queryIP):
            
            ip = queryIP.split(":")
            
            if len(ip) != 8:
                return False
            
            for sub in ip:
                if len(sub) == 0:
                    return False
                if len(sub) > 4:
                    return False
                
                for char in sub:
                    if not char.isdigit() and not char in values:
                        return False
                  
            return True
                    
        if ipv4(queryIP):
            return "IPv4"
        
        if ipv6(queryIP):
            return "IPv6"
        
        return "Neither"