class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        left = nums[0]
        mid = nums[1]
        max_diff = left - mid
        for k in range(2,n):
            if nums[k-2]>left:
                left = max(left,nums[k-2])
                mid = nums[k-1]
            mid = min(mid,nums[k-1])
            max_diff = max(max_diff,left-mid)
            res = max(res,max_diff*nums[k])
        return res
