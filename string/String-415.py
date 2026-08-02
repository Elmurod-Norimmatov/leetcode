# ACCEPTED

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        s = ""
        temp = 0
        while i > -1 or j > -1:
            if i > -1 and j > -1:
                curr = int(num1[i]) + int(num2[j]) + temp
                s = str(curr%10) + s
                temp = curr // 10
                i -= 1
                j -= 1
            elif i > -1:
                curr = int(num1[i]) + temp
                s = str(curr%10) + s
                temp = curr // 10
                i -= 1
            else:
                curr = int(num2[j]) + temp
                s = str(curr%10) + s
                temp = curr // 10
                j -= 1

        if temp == 1:
            s = '1' + s

        return s