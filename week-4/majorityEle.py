class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candidate1, candidate2 = 0, 1
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        for num in [candidate1, candidate2]:
            temp = 0
            for n in nums:
                if n == num:
                    temp += 1
            if temp>(len(nums)//3):
                ans.append(num)
        return ans