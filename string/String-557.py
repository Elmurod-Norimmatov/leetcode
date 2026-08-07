class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = ""
        i = 0
        j = 0
        while j < n:
            if j == n-1:
                res += s[i:][::-1]

            if s[j] == ' ':
                res += s[i:j][::-1] + ' '
                i = j+1

            j += 1
        return res

s = Solution()
print(s.reverseWords("Ding"))