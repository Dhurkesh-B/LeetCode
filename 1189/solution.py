class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = {'b':0, 'a':0, 'l':0,'o':0, 'n':0 }
        for i in text:
            if i in cnt:
                cnt[i]+=1
        res = min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])
        return res
