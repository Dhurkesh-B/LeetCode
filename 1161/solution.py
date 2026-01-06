class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 0        
        maxValue = float('-inf')
        q = deque()
        q.append(root)
        lev = 0
        while q:
            nextNode = []
            lev+=1
            total = 0
            while q:
                temp = q.popleft()
                total+=temp.val
                if temp.left:
                    nextNode.append(temp.left)
                if temp.right:
                    nextNode.append(temp.right)
            if total>maxValue:
                maxValue = total
                res = lev
            q+=nextNode
        return res
