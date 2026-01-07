class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sumValues = []
        mod = 10**9 + 7
        def func(node):
            value = node.val
            if node.left:
                value+=func(node.left)
            if node.right:
                value+=func(node.right)
            sumValues.append(value)            
            return value
        func(root)
        res = 0
        for i in range(len(sumValues)):
            res = max(res,(sumValues[-1]-sumValues[i])*sumValues[i])
        return res%mod
