# ACCEPTED

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Agar numRows = 1 bo'lsa
        if numRows == 1:
            return [[1]]

        # Agar numRows = 2 bo'lsa
        if numRows == 2:
            return [[1], [1, 1]]


        # Aks holda alogoritm ishga tushadi

        result = [[1], [1, 1]]

        for t in range(2, numRows):
            r = [1]
            temp = result[t-1]
            for i in range(1, len(temp)):
                r.append(temp[i-1]+temp[i])

            r.append(1)
            result.append(r)

        return result