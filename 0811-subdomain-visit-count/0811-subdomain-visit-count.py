class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        #access each element in extract the domain and the number of reption
        # combine specific domain with repetation and store on to the final result list
        
        
        final_res = {}
        for domain in cpdomains:
            new = domain.split()
         
            rep = new[0]
            domains = new[1]
         
            final_res[domains] = final_res.get(domains,0) + int(rep)
            
            result = []
            
            
            while domains.find(".")!= -1:
                location = domains.find(".")+1
             
                domains = domains[location:]
             
                final_res[domains] = final_res.get(domains,0) + int(rep)
                
            for pair in final_res:
                result.append(str(final_res[pair])+" "+pair)
                
                
        return result
        