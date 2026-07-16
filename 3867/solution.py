class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = nums[0]
        prefixGcd = []
        res = 0
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            prefixGcd.append(math.gcd(nums[i], mx))
        prefixGcd.sort()
        for i in range(len(prefixGcd)//2):
            res+=math.gcd(prefixGcd[i], prefixGcd[-(i+1)])
        return res
