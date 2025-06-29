
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        left = 0
        right = n-1
        mod = 10**9 + 7
        while left<=right:
            if nums[left]+nums[right]<=target:
                res+=pow(2,right-left,mod)
                left+=1
            else:
                right-=1
        return res%mod

