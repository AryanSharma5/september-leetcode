class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = currMax = currMin = nums[0]
        for i in range(1, len(nums)):
            currMax, currMin = max(currMax*nums[i], nums[i], currMin*nums[i]), min(currMin*nums[i], nums[i], currMax*nums[i])
            ans = max(ans, currMax)
        return ans