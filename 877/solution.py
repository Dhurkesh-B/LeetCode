class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        di = {}
        def dfs(left, right):
            if left==right:
                return piles[left]
            if (left, right) in di:
                return di[(left, right)]
            leftSide = piles[left] - dfs(left+1, right)
            rightSide = piles[right] - dfs(left, right-1)
            di[(left, right)] = max(leftSide, rightSide)
            return di[(left, right)]
        return dfs(0,len(piles)-1)>=1
