class Solution:
    # A will finds a way.
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        val = '1'
        for _ in range(n-1):
            i = 0
            temp = ''
            l = len(val)
            while i<l:
                cnt = 1
                j = i+1
                while j<l and val[i]==val[j]:
                    cnt+=1
                    j+=1
                temp = temp+str(cnt)+val[i]
                i = j
            val = temp
        return val
