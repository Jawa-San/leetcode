class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        substring = set()

        while right < len(s):
            if s[right] in substring:
                substring.discard(s[left])
                left += 1
            else:
                substring.add(s[right])
                right += 1
            res = max(res, right - left)
        return res
            

        