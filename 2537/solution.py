from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        di = defaultdict(int)
        res = 0
        left = 0
        right = 0
        n = len(nums)
        pair_count = 0
        while left<n:
            while right<n and pair_count<k:
                di[nums[right]]+=1
                if di[nums[right]]>1:
                     pair_count+=di[nums[right]]-1
                right+=1
            if pair_count>=k:
                res+=(n-right)+1
            di[nums[left]]-=1
            if di[nums[left]]>0:
                pair_count-=di[nums[left]]
            left+=1
        return res

            
