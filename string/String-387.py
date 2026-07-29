# ACCEPTED

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = set(s)
        res = -1
        for i in s1:
            if s.count(i) == 1:
                index = s.index(i)
                if index < res or res == -1:
                    res = index
        
        return res