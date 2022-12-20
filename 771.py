class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        map = {}

        for i, n in enumerate(jewels):
            map[n] = i
        
        for i in stones:
            if i in map:
                res += 1
                
        return res