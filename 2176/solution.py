class Solution:
    # It always seems impossible until it's done.
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    res+=1
        return res
