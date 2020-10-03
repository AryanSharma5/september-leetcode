class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7
        # \
        #  \             6
        #   \       5   / \
        #    \     / \ /   4
        #     \   /   3
        #      \ /
        #       1
        
        maxProfit = 0
        minStock = float('inf')
        for i in range(len(prices)):
            minStock = min(minStock, prices[i])  # buy minimum value stock today.
            if minStock < prices[i]:             # We can sell today to make profit.
                maxProfit = max(maxProfit, prices[i] - minStock)
        return maxProfit