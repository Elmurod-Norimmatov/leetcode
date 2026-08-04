# ACCEPTED

class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        if num == 0:
            return "0"

        minus = False
        
        if num < 0:
            minus = True
            num *= -1

        while num != 0:
            mod = num % 7
            num //= 7
            s = str(mod) + s

        if minus:
            s = '-' + s
        return s