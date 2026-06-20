class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1][0]!=n:
            restrictions.append([n,n-1])
        r = len(restrictions)
        for i in range(1,r):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1]+dist)
        for i in range(r-2,-1,-1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1]+dist)
        res = 0 
        for i in range(1,r):
            dist = restrictions[i][0] - restrictions[i-1][0]
            h1,h2 = restrictions[i-1][1], restrictions[i][1]
            res = max(res, (h1+h2+dist)//2)
        return res
