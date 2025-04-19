class Solution:
    # Don't watch the clock; do what it does. Keep going.
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0
        for i in range(n):
            left = i+1
            right = n-1
            ind1 = n
            ind2 = i
            mid = right
            while left<=right:
                mid = (left+right)//2
                if nums[mid]+nums[i]>=lower:
                    ind1 = min(ind1,mid)
                    right = mid-1
                else:                    
                    left = mid+1
            left  = i+1
            right = n-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]+nums[i]<=upper:
                    ind2 = max(ind2,mid)
                    left = mid+1
                else:
                    right = mid-1
            res+=max(0,ind2-ind1+1)
        return res
