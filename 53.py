class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        curr = 0
        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            sum = max(sum, curr)
        return sum