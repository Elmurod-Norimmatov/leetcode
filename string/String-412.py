# ACCEPTED

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        i = 0
        while i < n:
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                res.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                res.append("Fizz")
            elif (i+1) % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i+1))
            i += 1
            
        return res