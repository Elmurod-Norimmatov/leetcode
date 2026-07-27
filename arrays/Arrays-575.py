# ACCEPTED

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m = len(candyType) // 2
        s = len(set(candyType))
        return min(m,s)