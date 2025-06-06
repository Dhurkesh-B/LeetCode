from collections import defaultdict
class Solution:
    def robotWithString(self, s: str) -> str:
        di = defaultdict(int)
        res = ''
        temp = []
        for i in s:
            di[i]+=1
        for c in s:
            temp.append(c)
            di[c]-=1
            mi = 'a'
            while mi!='z' and di[mi]==0: 
                mi = chr(ord(mi)+1)
            while temp and temp[-1]<=mi:
                res+=temp.pop()
        return res
