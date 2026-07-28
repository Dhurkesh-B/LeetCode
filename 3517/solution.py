class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        res = ''
        mid = ''
        for i in sorted(count.keys()):
            if count[i]%2:
                mid = i 
                count[i]-=1
            res+=i*(count[i]//2)
        res = res + mid + res[::-1]
        return res
