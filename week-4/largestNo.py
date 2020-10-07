class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = set(tuple(nums))
        if len(s) == 1:
            if 0 in s:
                return '0'
        ans = self.mergesort(nums, 0, len(nums) - 1)
        return ''.join([str(i) for i in ans])
    
    def mergesort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = (l+r)//2
        left = self.mergesort(nums, l, mid)
        right = self.mergesort(nums, mid + 1, r)
        return self.merge(left, right)
    
    def merge(self, a, b):
        final, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if self.compare(a[i], b[j]):
                final.append(a[i])
                i += 1
            else:
                final.append(b[j])
                j += 1
        final.extend(a[i:])
        final.extend(b[j:])
        return final
                
    def compare(self, a, b):
        return str(a) + str(b) > str(b) + str(a)