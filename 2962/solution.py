class Solution(object):
    def countSubarrays(self, nums, k):
        res = 0
        l = 0
        cnt = 0
        mx = max(nums)
        for r in range(len(nums)):
            if nums[r]==mx:
                cnt+=1
            while cnt>k or (nums[l]!=mx and cnt==k and l<=r):
                if nums[l]==mx:
                    cnt-=1
                l+=1
            if cnt==k:
                res+=l+1
        return res

        
