class Solution:
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return False
        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        result = 0
        while nums and not self.isSorted(nums):
            ind = -1
            mini = float("inf")
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < mini:
                    ind = i
                    mini = nums[i] + nums[i + 1]
            nums[ind] += nums[ind + 1]
            nums.pop(ind + 1)
            result += 1
        return result
