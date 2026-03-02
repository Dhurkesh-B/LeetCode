class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zeros = []
        n = len(grid)
        for i in range(n):
            ind = n-1
            j = ind
            while ind>=0 and grid[i][ind]==0:
                ind-=1
            zeros.append(j-ind)
        result = 0
        for i in range(n):
            if zeros[i]<n-1-i:
                ind = i
                for j in range(i+1,n):
                    if zeros[j]>=n-1-i:
                        ind = j
                        break
                if ind==i:
                    return -1
                result+=ind-i
                for j in range(ind,i,-1):
                    zeros[j],zeros[j-1] = zeros[j-1],zeros[j]
        return result
