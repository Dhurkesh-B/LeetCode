from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            arr = nums[i:i+k]
            cnt = Counter(arr)
            value = 0
            for key in sorted(cnt.keys(),key = lambda x:(-cnt[x],-x))[:x]:
                value+=(key*cnt[key])
            res.append(value)
        return res

