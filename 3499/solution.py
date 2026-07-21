class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        curr = 0
        res = 0
        zeros = []
        for i in s:
            if i=='0':
                curr+=1
            elif curr:
                zeros.append(curr)
                curr = 0 
        if curr:
            zeros.append(curr)
            
        for i in range(1,len(zeros)):
            res = max(res, zeros[i-1]+zeros[i])

        return res+ones
