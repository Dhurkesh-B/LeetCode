from collections import defaultdict
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        res = 0 
        di = defaultdict(int)
        for i in nums:
            di[i]+=1
        for i in di.keys():
            if di[i]>1:
                count+=1
        while count>0 and len(nums)>=3:
            for i in range(res*3,min((res*3)+3,len(nums))):
                di[nums[i]]-=1
                if di[nums[i]]==1:
                    count-=1
            res+=1    
        if count:
            res+=1
        return res
                

        
