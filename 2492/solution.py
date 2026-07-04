class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, nei, dist in roads:
            adj[src].append((nei,dist))
            adj[nei].append((src,dist))
        res = float('inf')
        vis = set()
        def dfs(i):
            if i in vis:
                return 
            vis.add(i)
            nonlocal res
            for nei, dist in adj[i]:
                res = min(res,dist)
                dfs(nei)
        dfs(1)
        return res
            
