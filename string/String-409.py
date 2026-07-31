# ACCEPTED

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        ones = 0

        s1 = set(s)

        for i in s1:
            cnt = s.count(i)
            if cnt % 2 == 1:
                ones = 1
                res += cnt - 1
            else:
                res += cnt

        return res + ones