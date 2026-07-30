# ACCEPTED

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        for i in range(len(s)):
            if s[i] not in d.keys() and t[i] not in d.values():
                d[s[i]] = t[i]

            if s[i] not in d.keys() or t[i] not in d.values():
                return False

            if d[s[i]] != t[i]:
                return False

            continue

        return True