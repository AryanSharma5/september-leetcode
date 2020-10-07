class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=min(nums):
            return 0
        left, ans, prod = 0, 0, 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod>=k:
                prod //= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans