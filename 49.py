class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            res = ''.join(sorted(i))
            if res not in map:
                map[res] = [i]
            else:
                map[res].append(i)

        return map.values()
            

            # if sorted strs[i] is not in the map:
            #   add sorted strs[i] to map as a key
            #   make a new list and associate it with the key
            # else 
            #   add it to its respective list