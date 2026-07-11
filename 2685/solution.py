class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        paths = defaultdict(list)
        for u,v in edges:
            paths[u].append(v)
            paths[v].append(u)
        vis = set()
        def dfs(node):
            vis.add(node)
            nodeCnt = 1
            edgeCnt = len(paths[node])
            for nei in paths[node]:
                if nei not in vis:
                    nd, ed = dfs(nei)
                    nodeCnt+=nd
                    edgeCnt+=ed 
            return nodeCnt, edgeCnt
        res = 0
        for i in range(n):
            if i in vis:
                continue
            m, e = dfs(i)
            e//=2 
            if e==m*(m-1)//2:
                res+=1
        return res
