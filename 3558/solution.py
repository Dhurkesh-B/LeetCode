class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        emap = defaultdict(list)
        depth = {1:0}
        mod = 10**9 + 7
        maxDepth = 0
        for u,v in edges:
            u,v = sorted([u,v])
            emap[u].append(v)
        q = [1]
        while q:
            node = q.pop(0)
            for child in emap[node]:
                depth[child] = depth[node]+1 
                maxDepth = max(maxDepth, depth[child])
                q.append(child)
        res = (2**(maxDepth-1))%mod
        return res
