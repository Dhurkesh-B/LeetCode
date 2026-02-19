class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        curr = 1
        s+='2'
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                curr+=1
            else:
                result+=min(prev,curr)
                prev = curr
                curr = 1
        return result
