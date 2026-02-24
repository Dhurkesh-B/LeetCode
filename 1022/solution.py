# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def traverse(root,s):
            if not root:
                return            
            s+=str(root.val)
            if not (root.left or root.right):
                nonlocal result
                result+=int(s,2)
            traverse(root.left,s)
            traverse(root.right,s)
        traverse(root,'')
        return result
            
