# ACCEPTED

class Solution:
    def check(self, letter):
        if letter.lower() in "qwertyuiop":
            return 1
        if letter.lower() in "asdfghjkl":
            return 2
        if letter.lower() in "zxcvbnm":
            return 3

    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            g = self.check(word[0])
            for letter in word:
                if self.check(letter) == g:
                    continue
                else:
                    g = 0
                    break

            if g != 0:
                ans.append(word)

        return ans