class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(curr):
            count = 0
            i = 0 
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=curr:
                    count+=1
                    i+=1
                i+=1
                if count==p:
                    return True
            return False
        if p==0: return p
        nums.sort()
        left,right = 0,10**9
        res = 10**9
        while left<=right:
            mid = (left+right)//2
            if isValid(mid):
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res
