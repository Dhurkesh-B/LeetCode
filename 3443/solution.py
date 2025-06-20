class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = {'N':0, 'S':0, 'E':0, 'W':0}
        direct = {'N':-1,'S':1,'E':1,'W':-1}
        res = 0
        side = 0
        updown = 0
        for i in s:
            if i in 'EW':
                side+=direct[i]
            else:
                updown+=direct[i]
            counter[i]+=1
            total = min(counter['E'],counter['W'])+ min(counter['N'],counter['S'])
            if total<=k:
                res = max(res,abs(side)+abs(updown)+(2*total))
            else:
                res = max(res,abs(side)+abs(updown)+(2*k))

        return res
        
