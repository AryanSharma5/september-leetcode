class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        def buildTrie(num):
            curr = trie
            for bit in format(num, '032b'):
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]
            curr['endVal'] = num
            return
        def search(num):
            curr = trie
            for bit in format(num, '032b'):
                rev = '0' if bit == '1' else '1'
                if rev in curr:
                    curr = curr[rev]
                else:
                    curr = curr[bit]
            return curr['endVal']
        for num in nums:
            buildTrie(num)
        ans = 0
        for num in nums:
            ans = max(ans, num^search(num))
        return ans