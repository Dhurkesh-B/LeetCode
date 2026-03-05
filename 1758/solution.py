class Solution:
    def minOperations(self, s: str) -> int:
        firstZero = 0
        firstOne = 0
        for i in range(len(s)):
            if i%2:
                if s[i]=='0':
                    firstZero+=1
                else:
                    firstOne+=1
            elif i%2==0:
                if s[i]=='1':
                    firstZero+=1
                else:
                    firstOne+=1
        return min(firstZero, firstOne)
