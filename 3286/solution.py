class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        best = {}
        def dfs(r,c,health):
            if r==len(grid)-1 and c==len(grid[0])-1:
                return health>0
            if health<=0:
                return False
            if (r,c) in best and best[(r,c)]>=health:
                return False
            best[(r,c)] = health
            if r+1<len(grid):
                if dfs(r+1,c,health-grid[r+1][c]):
                    return True
            if r-1>=0:
                if dfs(r-1,c,health-grid[r-1][c]):
                    return True
            if c+1<len(grid[0]):
                if dfs(r,c+1,health-grid[r][c+1]):
                    return True
            if c-1>=0:
                if dfs(r,c-1,health-grid[r][c-1]):
                    return True
            return False

        return dfs(0,0,health-grid[0][0])

