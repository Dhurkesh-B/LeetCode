from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        di = defaultdict(int)
        total = len(set(nums))
        count = 0
        res = 0
        n = len(nums)
        left,right = 0,0
        while left<n and left<=right:
            while right<n and count<total:
                di[nums[right]]+=1
                if di[nums[right]]==1:
                    count+=1
                right+=1
            if count==total:
                res = res +(n-(right-1))
            di[nums[left]]-=1
            if di[nums[left]]==0:
                count-=1
                del di[nums[left]]
            left+=1
        return res
