class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i, n in enumerate(nums):
            if nums[i] in map:
                return True
            map[nums[i]] = n
        return False

