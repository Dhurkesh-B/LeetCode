class Solution:
    def maxProduct(self, n: int) -> int:
        res = 0
        m = 0
        while n:
            d = n%10
            res = max(res, d*m)
            m = max(m, d)
            n//=10
        return res
