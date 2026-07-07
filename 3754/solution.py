class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, tot, i = 0, 0, 1 
        while n:
            d = n%10 
            n//=10 
            if not d:
                continue
            x = d*i + x
            tot+=d 
            i*=10
        return x*tot
