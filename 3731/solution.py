class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxValue = float('-inf')
        minValue = float('inf')
        vis = set()
        for i in nums:
            maxValue = max(maxValue, i)
            minValue = min(minValue, i)
            vis.add(i)
        
        res = []
        for i in range(minValue,maxValue):
            if not i in vis:
                res.append(i)
        return res
