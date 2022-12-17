class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
            if t[i] in map2:
                map2[t[i]] += 1
            else:
                map2[t[i]] = 1
        if map == map2:
            return True
                
        return False