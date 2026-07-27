# ACCEPTED

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        a = []
        for i in range(n):
            if i == 0:
                a.append(nums[i])
                continue

            if nums[i] - 1 == nums[i-1]:
                a.append(nums[i])
            else:
                res.append(a)
                a = []
                a.append(nums[i])

        if a:
            res.append(a)

        for i in range(len(res)):
            if len(res[i]) == 1:
                res[i] = f"{res[i][0]}"
            else:
                res[i] = f"{res[i][0]}->{res[i][-1]}"

        return res