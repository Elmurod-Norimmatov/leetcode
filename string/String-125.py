# ACCEPTED

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = 'abcdefghijklmnopqrstuvwxyz1234567890'

        s2 = ''
        for i in s:
            if i.lower() in s1:
                s2 += i.lower()

        return s2 == s2[::-1]