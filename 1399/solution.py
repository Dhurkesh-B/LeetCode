from collections import defaultdict
class Solution:
    def countSum(self, n: int)->int:
        count = 0
        for i in str(n):
            count+=int(i)
        return count
    def countLargestGroup(self, n: int) -> int:
        di = defaultdict(int)
        res = 0
        mx = 0
        for i in range(1,n+1):
            val = self.countSum(i)
            di[val]+=1
            mx = max(mx,di[val])
        for i in di.keys():
            if di[i]==mx:
                res+=1
        return res
