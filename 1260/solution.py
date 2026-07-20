class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in grid:
            arr+=i
        n = len(arr)
        k = k%n
        col = len(grid[0])
        arr = arr[n-k:]+arr[:n-k]
        for i in range(n):
            grid[i//col][i%col] = arr[i]
        return grid
