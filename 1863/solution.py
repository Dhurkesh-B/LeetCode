class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def func(curr,ind):
            nonlocal res
            if ind<len(nums):
                res+=(curr^nums[ind])
                func(curr,ind+1)                
                func(curr^nums[ind],ind+1)
        func(0,0)
        return res
