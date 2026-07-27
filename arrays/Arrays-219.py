# TIME LIMIT

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l == 1:
            return False

        if l <= k:
            if len(nums) != len(list(set(nums))):
                return True
            return False

        n = l - (k-1)

        for i in range(n):
            t = nums[i:(i+k+1)]

            if len(t) != len(list(set(t))):
                return True

        return False


s = Solution()
print(s.containsNearbyDuplicate())