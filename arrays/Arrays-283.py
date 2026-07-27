# ACCEPTED

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = [0] * nums.count(0)
        if len(zeros) == len(nums):
            return nums
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                if nums[i+1:] == zeros:
                    break

                i += 1

        return nums