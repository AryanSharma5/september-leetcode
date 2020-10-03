class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = currMax = currMin = nums[0]
        for i in range(1, len(nums)):
            currMax, currMin = max(currMax*nums[i], nums[i], currMin*nums[i]), min(currMin*nums[i], nums[i], currMax*nums[i])
            ans = max(ans, currMax)
        return ans

# class Trie:
# 	trie = {}
# 	def updateTrie(self, word):
# 		cur = self.trie
# 		print(bin(word)[2:])
# 		for x in format(word, '032b'):
# 			if x not in cur:
# 				cur[x] = {}
# 			cur = cur[x]
# 		cur['val'] = word
# 		return
# 	def searchComplement(self, word):
# 		cur = self.trie
# 		for x in format(word, '032b'):
# 			rev = '0' if x=='1' else '1'
# 			if rev in cur:
# 				cur = cur[rev]
# 			else:
# 				cur = cur[x]
# 		return cur['val']

# obj = Trie()
# nums = [3, 10, 5, 100, 2, 8]
# for x in nums:
# 	obj.updateTrie(x)
# ans = 0
# print(obj.trie)
# for x in nums:
# 	ans = max(ans, x^obj.searchComplement(x))
# print(ans)