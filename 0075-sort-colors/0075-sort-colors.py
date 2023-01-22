class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0]*3
        for x in nums:
            temp[x] += 1
        i=0
        print(temp,'temp')
        for x in range(len(temp)):
            if temp[x] > 0:
                for _ in range(temp[x]):

                    nums[i] = x
                    i+=1
                    