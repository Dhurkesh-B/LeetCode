class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr = 0
        left = 0
        res = 0
        n = len(nums)
        for right in range(n):
            curr+=nums[right]
            while (curr*(right-left+1))>=k:
                curr-=nums[left]
                left+=1
            res+=(right-left+1)   
        return res
