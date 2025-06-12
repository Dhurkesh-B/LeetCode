class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        nums.insert(0,nums[0])
        nums.append(nums[0])
        for i in range(1,len(nums)):
            res  = max(res,abs(nums[i]-nums[i-1]))
        return res
        
