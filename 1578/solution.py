class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        res = 0
        n = len(colors)
        while i<n:
            total = neededTime[i]
            maxi = total
            while i+1<n and colors[i]==colors[i+1]:
                i+=1
                total+=neededTime[i]
                maxi = max(maxi,neededTime[i])
            i+=1
            res+=(total-maxi)
        return res
