class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        vis  = set()
        for i in nums[::-1]:
            curr = set()
            curr.add(i)
            for j in vis:
                curr.add(i+j)
            vis = vis|curr
        return int(total//2) in vis
