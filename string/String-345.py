# ACCEPTED

class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "AaEeIiOoUu"
        res1 = ""
        res2 = ""
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in VOWELS:
                res1 += s[i]
                i += 1
            if s[j] not in VOWELS:
                res2 = s[j] + res2
                j -= 1
            if s[i] in VOWELS and s[j] in VOWELS and i < j:
                res1 += s[j]
                res2 = s[i] + res2
                i += 1
                j -= 1
        ans = res1 + res2
        if len(s) > len(ans):
            ans = res1 + s[i] + res2
        return ans