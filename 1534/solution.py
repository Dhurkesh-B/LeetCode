class Solution:
    def countGoodTriplets(self, nums: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(nums[i]-nums[j])<=a and abs(nums[j]-nums[k])<=b and abs(nums[i]-nums[k])<=c:
                        count+=1
        return count

        
