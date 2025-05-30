from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        edge = defaultdict(list)
        for i in range(len(edges)):
            if edges[i]!=-1:
                edge[i].append(edges[i])
        res = [float('inf'),-1]

        def dfs(node1,curr,count,nodedict):
            for nei in edge[curr]:
                if not nei in nodedict:
                    nodedict[nei] = count+1
                    dfs(node1,nei,count+1,nodedict)
            return nodedict


        node1dict = dfs(node1,node1,0,defaultdict(int))
        node2dict = dfs(node2,node2,0,defaultdict(int))
        node1dict[node1] = 0
        node2dict[node2] = 0
        
        for node in range(len(edges)):
            if node in node2dict and node in node1dict:
                dist = max(node1dict[node],node2dict[node])
                if dist<res[0]:
                    res[0] = dist
                    res[1] = node
        return res[1]
