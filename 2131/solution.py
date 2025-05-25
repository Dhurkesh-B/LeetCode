from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        di = defaultdict(int)
        for i in words:
            di[i]+=1
        res = 0
        rem = False
        for word in di:
            rev = word[::-1]
            if word!=rev and rev in di:
                pair = min(di[word],di[rev])
                res+=pair*4
                di[word]-=pair
                di[rev]-=pair
            elif word==rev:
                pair = di[word]//2
                res+=pair*4
                di[word]-=pair*2
                if di[word]>0:
                    rem = True
        if res%4==0 and rem:
            res+=2
        return res
