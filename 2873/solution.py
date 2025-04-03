class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        i = 0     
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                i = j
            else:
                for k in range(j+1,n):
                    res = max(res,(nums[i]-nums[j])*nums[k])
        return res