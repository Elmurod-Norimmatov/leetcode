# ACCEPTED

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v, h = 0, 0
        for i in moves:
            if i == "U":
                v += 1
            if i == "D":
                v -= 1
            if i == "L":
                h -= 1
            if i == "R":
                h += 1
        return v == 0 and h == 0