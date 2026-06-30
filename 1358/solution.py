class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        di = {'a':0, 'b':0, 'c':0}
        res = 0
        l = 0 
        for r in range(len(s)):
            di[s[r]]+=1
            while di['a']>=1 and di['b']>=1 and di['c']>=1:
                res+=(len(s)-r)
                di[s[l]]-=1
                l+=1
        return res
