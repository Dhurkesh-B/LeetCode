class Solution:
    def clearStars(self, s: str) -> str:
        counter = [[] for _ in range(26)]
        s = list(s)
        res = ''
        for i,c in enumerate(s):
            if c=='*':
                for j in range(26):
                    if counter[j]:
                        ind = counter[j].pop()
                        s[ind] = '*'
                        break
            else:
                counter[ord(c)-ord('a')].append(i)
        for c in s:
            if c!='*':
                res+=c
        return res
