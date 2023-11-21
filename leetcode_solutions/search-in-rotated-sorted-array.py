class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = -1
        right = len(nums)

        while right > left + 1:

            md = left + (right - left) // 2
            print(md,"md")
            if nums[md] > nums[md - 1] and nums[md] > nums[-1]: #mountain
                left = md
            else:
                right = md

        peak = left
        print(peak)
        def binarySearch(left,right):
            while right > left + 1:
                
                md = left + (right - left) // 2
                print(md,"second")
                if nums[md] < target: #mountain
                    left = md

                if nums[md] >= target:
                    right = md

            return right

        first,second = binarySearch(-1,peak + 1),binarySearch(peak,len(nums))
        if 0 <= first < len(nums) and nums[first] == target: return first
        if 0 <= second < len(nums) and nums[second] == target: return second
        return -1

       

         
        