class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row,col = len(grid),len(grid[0])
        prefix = 1
        suffix = 1
        result = [[1]*col for _ in range(row)]
        mod = 12345 
        for i in range(row):
            for j in range(col):
                result[i][j] = prefix 
                prefix = (prefix*grid[i][j])%mod

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                result[i][j]= (result[i][j]*suffix)%mod
                suffix = (suffix*grid[i][j])%mod 
        return result 
