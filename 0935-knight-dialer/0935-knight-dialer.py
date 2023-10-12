class Solution:
    def knightDialer(self, n: int) -> int:
        #let's try bottom up
        
        dp = [{i : 0 for i in range(10)} for _ in range(n)]
        moves = [[4,6],[6,8],[7,9],[8,4],[9,0,3],[],[7,1,0],[6,2],[3,1],[2,4]]
        Mod = (10 ** 9 + 7)
        #base case
        for key in dp[0]:
            dp[0][key] = 1
            
        for i in range(1,n):
            prev = dp[i - 1]
            for key in dp[i]:#key 0 1 2 3
                for move in moves[key]:
                    dp[i][key] += prev[move]
                
        ans = dp[n - 1]
        total = 0
        for key in ans:
            total += ans[key]
            
        return total % Mod
        
        