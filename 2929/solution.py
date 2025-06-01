class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for p1 in range(min(n,limit)+1):
            rem = n - p1
            if rem>2*limit:
                continue
            p2 = min(limit,rem)
            p3 = rem - p2
            res+=(p2-p3+1)
        return res 
