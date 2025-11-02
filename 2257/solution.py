class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['']*n for _ in range(m)]
        result = 0
        for r,c in guards:
            grid[r][c] = 'g'
        for r,c in walls:
            grid[r][c] = 'w'
        
        for r,c in guards:
            cc = c-1
            #left
            while cc>=0 and grid[r][cc] not in ['g','w']:
                grid[r][cc] = 'o'
                cc-=1
            cc = c+1
            #right
            while cc<n and grid[r][cc] not in ['g','w']:
                grid[r][cc] = 'o'
                cc+=1
            cr = r-1
            #top
            while cr>=0 and grid[cr][c] not in ['g','w']:
                grid[cr][c] = 'o' 
                cr-=1
            cr = r+1
            #bottom
            while cr<m and grid[cr][c] not in ['g','w']:
                grid[cr][c] = 'o'
                cr+=1
        
        for cnt in grid:
            result+=cnt.count('')
        return result
