class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        mapp = {}
        q = deque()
        q.append((1,0,-1))
        while q:
            node, lvl, par = q.popleft()
            mapp[node] = (lvl, par)
            for nei in adj[node]:
                if nei!=par:
                    q.append((nei, lvl+1,node))
        @cache
        def lca(a,b):
            while mapp[a][0]>mapp[b][0]: a=mapp[a][1]
            while mapp[a][0]<mapp[b][0]: b=mapp[b][1]
            while a!=b:
                a=mapp[a][1]
                b=mapp[b][1]
            return a

        res = []
        for a,b in queries:
            l = lca(a,b)
            lvl = (mapp[a][0]-mapp[l][0])+(mapp[b][0]-mapp[l][0])
            res.append(0 if lvl==0 else pow(2,lvl-1,10**9+7))
        return res

