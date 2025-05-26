from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
        dp = [[0] * 26 for _ in range(n)]  # dp[i][c] = max count of color c at node i
        self.res = 0
        self.has_cycle = False

        def dfs(node):
            if visited[node] == 1:
                self.has_cycle = True
                return
            if visited[node] == 2:
                return

            visited[node] = 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] = 1

            for nei in graph[node]:
                dfs(nei)
                if self.has_cycle:
                    return
                for c in range(26):
                    dp[node][c] = max(dp[node][c], dp[nei][c] + (1 if c == color_index else 0))

            self.res = max(self.res, max(dp[node]))
            visited[node] = 2

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                if self.has_cycle:
                    return -1

        return self.res
