from collections import defaultdict
class Solution:
    def bfsK(self,graph,node,k):
        q = [(node,0)]
        res = set()
        vis = set()
        while q:
            node,depth = q.pop(0)
            if node in vis or depth>k:
                continue
            vis.add(node)
            res.add(node)
            for nei in graph[node]:
                q.append((nei,depth+1))
        return res 
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        dist1 = defaultdict(int)
        dist2 = defaultdict(int)
        nodes1 = defaultdict(list)
        nodes2 = defaultdict(list)
        count2 = []
        mxn = 0
        res = []
        for u,v in edges1:
            nodes1[u].append(v)
            nodes1[v].append(u)
            mxn = max(mxn,u,v)
        for u,v in edges2:
            nodes2[u].append(v)
            nodes2[v].append(u)
        
        for node in nodes2.keys():
            count2.append(len(self.bfsK(nodes2,node,k-1)))
        
        mx = max(count2)
        for node in range(mxn+1):
            res.append(len(self.bfsK(nodes1,node,k))+mx)
        return res

