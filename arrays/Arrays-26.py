# ACCEPTED

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # set manfiy sonlarni oxirga o'tkazadi shuning uchun listni sortlash kerak
        s_nums = sorted(list(set(nums)))

        # Bu qismda nums o'zgartirib qo'yiladi, nums ni leetcodening o'zi tekshiradi
        for i in range(len(s_nums)):
            nums[i] = s_nums[i]

        return len(s_nums)