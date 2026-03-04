class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    cnt = 0
                    for c in range(col):
                        if mat[i][c]==1:
                            cnt+=1
                    if cnt==1:
                        for r in range(row):
                            if mat[r][j]==1:
                                cnt+=1
                        if cnt==2:
                            result+=1
        return result

