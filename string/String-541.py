# ACCEPTED

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        i = 0
        while i < n:
            if len(s[i:]) < k:
                res += s[i:][::-1]
            elif k <= len(s[i:]) < 2*k:
                res += s[i:i+k][::-1]
                res += s[i+k:]
            else:
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
            i += 2*k
        
        return res