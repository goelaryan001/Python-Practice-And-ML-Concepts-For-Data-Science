# For each pair of characters:
# 1. If s-char was already mapped, verify it maps to current t-char.
# 2. If t-char was already mapped, verify it maps back to current s-char.
# 3. Otherwise create the mapping in both directions.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS={}, {}
        for i in range(len(s)):
            c1,c2= s[i],t[i]
            if((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            mapST[c1]=c2
            mapTS[c2]=c1
        return True