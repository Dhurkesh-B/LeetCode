class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        cnt = 0 
        res = 0 
        for i in sorted(counter.keys(), key = lambda x:-counter[x]):
            res+=counter[i]*(1+cnt//8)
            cnt+=1 
        return res
