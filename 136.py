class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                return nums[l]
            else:
                l += 2
                r += 2
        return nums[r-1]
            
        

        