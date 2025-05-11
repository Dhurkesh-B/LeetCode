class Solution:
    def threeConsecutiveOdds(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            if nums[i]%2==nums[i+1]%2==nums[i+2]%2==1:
                return True
        return False
