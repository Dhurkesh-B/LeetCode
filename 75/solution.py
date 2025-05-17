from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        di=defaultdict(int)
        for i in nums:
            di[i]+=1
        res=[]
        while di:
            m=min(di)
            for _ in range(di[m]):
                res.append(m)
            del di[m]
        for i in range(len(nums)):
            nums[i]=res[i]
