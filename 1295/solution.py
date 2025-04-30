class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res+=(len(str(i))%2==0)
        return res
        
