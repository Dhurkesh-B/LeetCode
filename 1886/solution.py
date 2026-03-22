class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat==target:
                return True  
            arr = [[0]*n for i in range(n)]           
            for i in range(n):
                for j in range(n):
                    arr[j][n-1-i] = mat[i][j]
            mat = arr.copy()              
        return False
