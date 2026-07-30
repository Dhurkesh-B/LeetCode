class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0 
        for i in range(len(word)):
            res+=1+i//8
        return res
