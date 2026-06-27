from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = cnt.get(1,0)
        if res and res%2==0:
            res-=1
        for i in cnt:
            x = i
            sq = int(x**0.5)
            if sq*sq==x and cnt.get(sq,0)>1:
                continue
            temp = 0
            while x<=31622 and cnt.get(x,0)>1:
                temp+=2
                x*=x
            if cnt.get(x,0)>=1:
                temp+=1
            else:
                temp-=1
            res = max(res, temp)
        return res
