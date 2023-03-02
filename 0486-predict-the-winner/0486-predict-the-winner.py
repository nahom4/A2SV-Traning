class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        turn = 1
        left = 0
        right = len(nums) - 1
        player1 = 0
        player2 = 0

        
        def game(nums,left,right,player1,player2,turn):

            if left > right:
                return player1 >= player2

            if turn:
                return game(nums,left + 1,right,player1 + nums[left],player2,turn - 1) or game(nums,left,right - 1,player1 + nums[right],player2,turn - 1) 
            return game(nums,left + 1,right,player1,player2 + nums[left],turn + 1) and game(nums,left,right - 1,player1,player2 + nums[right],turn + 1) 

        return game(nums,left,right,player1,player2,turn)