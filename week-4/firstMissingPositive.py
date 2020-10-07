class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        containsOne = False
        for i in range(len(nums)):
            if nums[i] == 1:
                containsOne = True
            elif nums[i]<=0 or nums[i]>len(nums):
                nums[i] = 1
        if not containsOne:
            return 1
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1*nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums) + 1