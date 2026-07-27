# ACCEPTED

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        temp = []
        for i in mat:
            temp += i

        if r == 1:
            return [temp]

        l = 0
        res = []
        while l < len(temp):
            res.append(temp[l:l+c])
            l += c

        return res