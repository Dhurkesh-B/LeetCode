class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        child = [[] for _ in range(n)]
        for p,c in invocations:
            child[p].append(c)    
        q = deque([k])
        sus = [False] * n
        sus[k] = True 
        while q:
            node = q.popleft()
            for c in child[node]:
                if not sus[c]:
                    sus[c] = True
                    q.append(c)            
    
        for u,v in invocations:
            if sus[u]==False and sus[v]:
                return list(range(n))        
        return [i for i in range(n) if not sus[i]]
