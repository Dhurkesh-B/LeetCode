class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i = 0
        res = []
        while i+(k-1)<len(s):
            res.append(s[i:i+k])
            i+=k
        if i<len(s):
            temp = s[i:]
            temp = temp + fill*(k-len(temp))
            res.append(temp)
        return res
