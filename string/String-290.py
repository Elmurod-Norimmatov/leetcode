# ACCEPTED

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d.keys() and s[i] not in d.values():
                d[pattern[i]] = s[i]
                continue

            if pattern[i] not in d.keys() or s[i] not in d.values():
                return False

            if d[pattern[i]] != s[i]:
                return False

            continue

        return True