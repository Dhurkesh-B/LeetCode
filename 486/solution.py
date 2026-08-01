class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def dfs(left, right):
            if left==right:
                return nums[left]
            leftSide = nums[left] - dfs(left+1, right)
            rightSide = nums[right] - dfs(left, right-1)

            return max(leftSide, rightSide)
        res = dfs(0, len(nums)-1)>=0
        return res
