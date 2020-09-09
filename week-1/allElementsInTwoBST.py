# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(root, first = False):
            if root:
                helper(root.left)
                if first:
                    self.ans1.append(root.val)
                else:
                    self.ans2.append(root.val)
                helper(root.right)
        self.ans1, self.ans2 = [], []
        helper(root1, first = True)
        helper(root2)
        return sorted(self.ans1 + self.ans2)