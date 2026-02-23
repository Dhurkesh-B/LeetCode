class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        vis = {s[i:i+k] for i in range(len(s)-k+1)}
        
        def strings(curr):
            if len(curr)==k:
                return curr in vis
            return strings(curr+'0') and strings(curr+'1')
        return strings('')
