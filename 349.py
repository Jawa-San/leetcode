class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = set()
        list = []
        
        for i in range(len(nums1)):
            if nums1[i] not in map:
                map.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in map:
                list.append(nums2[i])
                map.discard(nums2[i])
        return list
        