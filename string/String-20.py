# ACCEPTED

class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        if s[-1] == '(' or s[-1] == '{' or s[-1] == '[':
            return False

        if len(s) % 2 != 0:
            return False

        temp = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)

            if i == ')' or i == '}' or i == ']':
                temp.append(i)
                if temp[-2:] == ['(', ')'] or temp[-2:] == ['{', '}'] or temp[-2:] == ['[', ']']:
                    temp.pop(-1)
                    temp.pop(-1)
                else:
                    return False

        if temp:
            return False
        else:
            return True