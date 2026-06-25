from collections import defaultdict
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            di = defaultdict(int)
            for j in range(i, len(nums)):
                di[nums[j]]+=1
                if 2*di[target]>j-i+1:
                    res+=1
        return res
