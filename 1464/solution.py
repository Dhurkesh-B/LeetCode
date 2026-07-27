class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = -1, -1
        for i in nums:
            if i-1>max1:
                max2 = max1
                max1 = i-1
            elif i-1>max2:
                max2 = i-1 
        return max1*max2 
