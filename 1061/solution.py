from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        di = defaultdict(set)
        charmap = defaultdict(str)
        res = ''
        smallestMap = defaultdict(str)
        for i in range(len(s1)):
            u,v = s1[i],s2[i]
            if u==v:
                continue
            if v in charmap and u in charmap:
                grp_u ,grp_v = charmap[u], charmap[v]
                if grp_u==grp_v:
                    continue
                newMap = di[charmap[u]] | di[charmap[v]] | {u,v}
                new_leader = min(grp_u,grp_v)
                del di[grp_u]
                del di[grp_v]
                for c in newMap:
                    charmap[c] = new_leader
                di[new_leader] = newMap
            elif u in charmap:
                di[charmap[u]].add(v)
                charmap[v] = charmap[u]
            elif v in charmap:
                di[charmap[v]].add(u)
                charmap[u] = charmap[v]
            else:
                u,v = sorted([u,v])
                di[u] = {u,v}
                charmap[v] = u
                charmap[u] = u
        for i in charmap:
            di[charmap[i]].add(i)
        for i in di.keys():
            mi = min(di[i])
            for c in di[i]:
                smallestMap[c] = mi
        for i in baseStr:
            if i in smallestMap:
                res+=smallestMap[i]
            else:
                res+=i
        return res
