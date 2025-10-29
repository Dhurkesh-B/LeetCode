class Solution:
    def smallestNumber(self, n: int) -> int:
        l = len(bin(n)[2:])
        s = '1'*l
        while int(s,2)<n:
            s+='1'
        return int(s,2)
