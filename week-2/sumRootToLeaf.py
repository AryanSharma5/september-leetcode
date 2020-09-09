# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def helper(root, currNum, nums):
            if not root.left and not root.right:
                currNum += [root.val]
                nums.append(currNum)
                return
            if root.left:
                helper(root.left, currNum + [root.val], nums)
            if root.right:
                helper(root.right, currNum + [root.val], nums)
            return nums
        
        if not root:
            return 0
        if not root.left and not root.right:
            if root.val == 1:
                return 1
            return 0
        ans = 0
        for num in helper(root, [], []):
            ans += int(''.join(list(map(str, num))), 2)
        return ans