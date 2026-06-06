class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        total = sum(nums)
        res = []
        for i in nums:
            res.append(abs(left-(total-left-i)))
            left+=i
        return res
