# ACCEPTED

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False

        i = 0
        sub = ""
        while i < n // 2:
            sub += s[i]
            if n % len(sub) == 0:
                l = n // len(sub)
                if s == (sub * l):
                    return True
            i += 1

        return False