class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        left = 0
        s = bin(n)[2:]
        n = len(s)
        while left+1<n and s[left]=='0':
            left+=1
        for right in range(left+1,n):
            if s[right]=='1':
                result = max(result,right-left)
                left = right
        return result

