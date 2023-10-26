class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        #preprocess and count the number of pairs that
        #when they are multiplied form the product
        
        N = len(arr)
        hashMap = set(arr)
        factors = defaultdict(list)
        for num in arr:
            ct = 0
            for target in arr:
                pair = num // target
                if pair in hashMap:
                    if target * pair == num:
                        if not (target,pair) in factors:
                            factors[num].append((target,pair))

        @cache
        def buildTree(root):
            
            if len(factors[root]) == 0:
                return 1
            ct = 1
            for factor in factors[root]:
                res = buildTree(factor[0]) * buildTree(factor[1])
                ct += res
        
            return ct
        
        ans = 0
        Mod = (10 ** 9 + 7)
        for num in arr:
            ans += buildTree(num)
            
        return ans % Mod
                
                    
                
        