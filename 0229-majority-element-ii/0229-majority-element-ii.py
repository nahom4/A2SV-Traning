class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        N = len(nums)
        target = N // 3
        for key in count:
            if count[key] > target:
                ans.append(key)
                
        return ans
        