class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = []
        nums = sorted(nums)
        cache = {}
        def dfs(ind,prev):
            if len(nums)==ind:
                return []
            if (ind,prev) in cache:
                return cache[(ind,prev)]
            res = dfs(ind+1,prev)
            if nums[ind]%prev==0:
                temp = [nums[ind]]+dfs(ind+1,nums[ind])
                if len(temp)>len(res):
                    res = temp
            cache[(ind,prev)] = res
            return res
        return dfs(0,1)
