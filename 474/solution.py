class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        cache = {}
        
        def dfs(m,n,ind):
            if ind==len(strs):
                return 0
            if (m,n,ind) in cache:
                return cache[(m,n,ind)]
            
            cache[(m,n,ind)] = dfs(m,n,ind+1)

            cz = strs[ind].count('0')
            co = len(strs[ind])-cz

            if cz<=m and co<=n:
                cache[(m,n,ind)] = max(cache[(m,n,ind)],1+dfs(m-cz,n-co,ind+1))
            
            return cache[(m,n,ind)]
        
        return dfs(m,n,0)
