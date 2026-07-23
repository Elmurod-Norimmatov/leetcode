# ACCEPTED

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_nums = []
        for i in nums:
            if i != val:
                temp_nums.append(i)

        nums[:] = temp_nums

        return len(nums)