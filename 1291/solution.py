class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = len(str(low))
        u = len(str(high))
        s = '123456789'
        res = []
        for i in range(l, u+1):
            for j in range(10-i):
                k = int(s[j:j+i])
                if k>high:
                    break
                if k>=low:
                    res.append(k)
        return res
