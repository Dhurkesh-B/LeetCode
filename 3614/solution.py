class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            if c.isalpha():
                l+=1
            elif c=='*' and l:
                    l-=1
            elif c=='#':
                l*=2

        if k>=l:
            return '.'
            
        for c in reversed(s):
            if c.isalpha():
                if k+1==l:
                    return c 
                l-=1 
            elif c=='*':
                l+=1 
            elif c=='#':
                l//=2 
                k%=l
            elif c=='%':
                k = l-k-1
            
