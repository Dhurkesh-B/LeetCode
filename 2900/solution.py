class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        def func(curr,ind,prev):
            nonlocal res
            if len(curr)>len(res):
                res = curr
            if ind<len(groups):
                if len(curr)==0 or prev!=groups[ind]:
                    func(curr+[ind],ind+1,groups[ind])
                else:
                    func(curr,ind+1,prev)
            else:
                return 
        func([],0,0)
        for i in range(len(res)):
            res[i] = words[res[i]]
        return res
