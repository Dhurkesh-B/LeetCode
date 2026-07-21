class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        curr = 0
        prev = float('-inf')
        res = 0
        for i in s:
            if i=='0':
                curr+=1
            else:
                if curr:
                    res = max(res, curr+prev)
                    prev = curr 
                    curr = 0
                ones+=1    
        if curr:
            res = max(res, curr+prev)
        
        res+=ones
        return res
