# ACCEPTED

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        m = 0
        t = 0
        c = 0

        for i in range(1, len(prices)):
            c = prices[i] - prices[i-1]

            if m < t:
                m = t

            t += c

            if t < 0:
                t = 0

        return m if m > t else t