class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        incl, excl = nums[0], 0
        for i in range(1, len(nums)):
            temp = incl
            incl = max(incl, nums[i]+excl)
            excl = temp
        return max(incl, excl)