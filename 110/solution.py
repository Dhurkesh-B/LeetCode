# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def dfs(root, height):
            if root:
                left = dfs(root.left, height) + height + 1
                right = dfs(root.right, height) + height + 1
                if abs(left - right) >= 2:
                    result[0] = False
                return max(left, right)
            else:
                return 0

        dfs(root, 0)
        return result[0]
