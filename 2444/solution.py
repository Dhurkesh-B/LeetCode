from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        wrong = -1
        mi = -1
        mx = -1
        res = 0
        for i in range(len(nums)):
            if nums[i]>maxK or nums[i]<minK:
                wrong = i
            if nums[i]==minK:
                mi = i
            if nums[i]==maxK:
                mx = i
            res = res + max(0,min(mx,mi)-wrong)
        return res
