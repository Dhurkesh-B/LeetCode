class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-3+1):
            if (nums[i]+nums[i+2])*2==nums[i+1]:
                res+=1
        return res
