class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        def func(ind,curr):
            if ind==-1:
                nonlocal res
                res = max(res,len(curr))
            if ind>=0:
                if curr=='' or s[ind]=='0' or int(s[ind]+curr,2)<=k:
                    func(ind-1,s[ind]+curr)
                else:
                    func(ind-1,curr)
        func(len(s)-1,'')
        return res
