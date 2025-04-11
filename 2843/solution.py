class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low,high+1):
            i = str(i)
            n = len(i)//2
            if len(i)==2*n:
                cnt1 = 0
                cnt2 = 0
                for j in range(n):
                    cnt1+=int(i[j])
                for j in range(n,2*n):
                    cnt2+=int(i[j])
                if cnt1==cnt2:
                    res+=1
        return res
