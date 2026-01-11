class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def hist(heights):
            maxArea = 0
            stack = [] 
            for i, h in enumerate (heights):
                start = i
                while stack and stack [-1] [1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))
            for i, h in stack:
                maxArea = max(maxArea, h* (len (heights) - i))
            return maxArea

        row,col = len(matrix), len(matrix[0])
        ps = [[0]*col for _ in range(row)]
        for j in range(col):
            curr = 0
            for i in range(row):
                if matrix[i][j]=='1':
                    curr+=1
                else:
                    curr = 0
                ps[i][j] = curr
        res = 0

        for i in range(row):
            res = max(res, hist(ps[i]))
        return res
